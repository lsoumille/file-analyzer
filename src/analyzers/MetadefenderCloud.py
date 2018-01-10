import json

import time
import urllib3

from src.analyzers.IAnalyzer import IAnalyzer
from src.utils.ConfigHelper import ConfigHelper
from src.utils.Constants import Constants
from src.utils.FileHelper import FileHelper


class MetadefenderCloud(IAnalyzer):

    def __init__(self):
        self.name = "Metadefender Cloud analyzer"
        self.api_key = ""
        self.file_path = ""
        self.file_name = ""
        self.data_id = ""

    def get_conf(self, conf_file, file_path):
        return (ConfigHelper.getMetadefenderCloud(conf_file), file_path)

    def setup(self, tuple):
        if tuple[0]:
            self.api_key = tuple[0]
        if tuple[1]:
            self.file_path = tuple[1]


    def analyze(self):
        print("[*] Starting analyze of " + self.file_path)
        fh = FileHelper()
        self.file_name = fh.getFileName(self.file_path)
        with open(self.file_path, "rb") as fp:
            file_content = fp.read()
        headers = {'apikey': self.api_key, 'user_agent': 'mcl-metadefender-rest-sanitize-disabled-unarchive'}
        http = urllib3.PoolManager()
        response = http.request('POST', Constants.METADEFENDER_SENDING_URL, headers=headers, body=file_content)
        try:
            self.data_id = self.handleScanResponse(response)
        except Exception as error:
            print("Error when uploading file to Metadefender Cloud platform : " + repr(error))
            return
        print("[*] File upload to Metadefender Cloud (scan id = " + self.data_id + ")")

    def report(self, level):
        if not self.data_id:
            return (self.name, '')
        # Retrieve scan result
        header = {'apikey': self.api_key}

        while True:
            print("[*] Request Rapport (data id = " + self.data_id + ")")
            http = urllib3.PoolManager()
            response = http.request('GET', Constants.METADEFENDER_REPORT_URL + self.data_id, headers=header)
            response_content = self.handleReportResponse(response, level)
            if response_content != -1:
                print("[!] Rapport received ")
                return response_content
            time.sleep(30)

    def handleScanResponse(self, response):
        if response.status != 200 or json.loads(response.data.decode())['status'] != 'inqueue':
            raise Exception('Bad Response from Metadefender Cloud API: Check your internet connection or your API Key')
        else:
            return json.loads(response.data.decode())['data_id']

    # Return -1 if the report is not available
    # Else return the positive number
    def handleReportResponse(self, response, level):
        response_data = json.loads(response.data.decode())
        if response.status != 200 or response_data['process_info']['result'] == 'Processing':
            return -1
        elif level == Constants.SHORT_REPORTING:
            return self.createShortReport(response_data)
        elif level == Constants.MEDIUM_REPORTING:
            return self.createMediumReport(response_data)
        else:
            return self.createComprehensiveReport(response_data)

    def createShortReport(self, response_data):
        if response_data['scan_results']['total_detected_avs'] != 0:
            return (self.name, True)
        else:
            return (self.name, False)

    def createMediumReport(self, response_data):
        if response_data['scan_results']['total_detected_avs'] != 0:
            return (self.name, True)
        else:
            return (self.name, False)

    def createComprehensiveReport(self, response_data):
        content = self.metadefenderResultToStr(response_data)
        if response_data['scan_results']['total_detected_avs'] != 0:
            return (self.name, True, content)
        else:
            return (self.name, False, content)

    def metadefenderResultToStr(self, response_data):
        str_res = "[*] Metadefender Cloud report:\n"
        for scanner in response_data['scan_results']['scan_details']:
            str_res += "> " + scanner + " : [ Detected: " + str(
                response_data['scan_results']['scan_details'][scanner]['scan_result_i']) + " | Result: " + str(
                response_data['scan_results']['scan_details'][scanner]['threat_found']) + " ]\n"
        return str_res + "Metadefender platform detects " + str(
            response_data['scan_results']['total_detected_avs']) + " positive results for " + self.file_name + "\n[*] Metadefender Cloud report end"
