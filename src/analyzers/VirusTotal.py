import json
import time
from pip._vendor import requests

from src.utils.ConfigHelper import ConfigHelper
from src.utils.Constants import Constants
from src.utils.FileHelper import FileHelper
from src.analyzers.IAnalyzer import IAnalyzer


class VirusTotal(IAnalyzer):

    def __init__(self):
        self.name = "Virus total analyzer"
        self.api_key = ""
        self.file_path = ""
        self.file_name = ""
        self.scan_id = ""

    def get_conf(self, conf_file, file_path):
        return (ConfigHelper.getVirusTotalAPIKey(conf_file), file_path)

    def setup(self, tuple):
        if tuple[0]:
            self.api_key = tuple[0]
        if tuple[1]:
            self.file_path = tuple[1]


    def analyze(self):
        print("[*] Starting analyze of " + self.file_path)
        fh = FileHelper()
        self.file_name = fh.getFileName(self.file_path)
        params = {'apikey': self.api_key}
        files = {'file': (self.file_name, fh.openFile(self.file_path))}
        response = requests.post(Constants.VIRUSTOTAL_SENDING_URL, files=files, params=params)
        try:
            self.scan_id = self.handleScanResponse(response)
        except Exception as error:
            print("Error when uploading file to virus total platform : " + repr(error))
            return
        print("[*] File upload to Virus Total (scan id = " + self.scan_id + ")")

    def report(self, level):
        if not self.scan_id:
            return (self.name, '')
        # Retrieve scan result
        params = {'apikey': self.api_key, 'resource': self.scan_id}
        headers = {
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "gzip, Python"
        }
        while True:
            print("[*] Request Rapport (scan id = " + self.scan_id + ")")
            response = requests.get(Constants.VIRUSTOTAL_REPORT_URL,
                                    params=params, headers=headers)
            response_content = self.handleReportResponse(response, level)
            if response_content != -1:
                print("[!] Rapport received ")
                return response_content
            time.sleep(30)

    def handleScanResponse(self, response):
        if response.status_code != 200 or response.json()['response_code'] != 1:
            raise Exception('Bad Response from Virus Total API: Check your internet connection or your API Key')
        else:
            return response.json()['scan_id']

    #Return -1 if the report is not available
    #Else return the positive number
    def handleReportResponse(self, response, level):
        json_data = response.json()
        if json_data['response_code'] != 1:
            return -1
        elif level == Constants.SHORT_REPORTING:
            return self.createShortReport(json_data)
        elif level == Constants.MEDIUM_REPORTING:
            return self.createMediumReport(json_data)
        else:
            return self.createComprehensiveReport(json_data)

    def createShortReport(self, json_data):
        if json_data['positives'] != 0:
            return (self.name, True)
        else:
            return (self.name, False)

    def createMediumReport(self, json_data):
        if json_data['positives'] != 0:
            return (self.name, True)
        else:
            return (self.name, False)

    def createComprehensiveReport(self, json_data):
        content = self.virusTotalResultToStr(json_data)
        if json_data['positives'] != 0:
            return (self.name, True, content)
        else:
            return (self.name, False, content)

    def virusTotalResultToStr(self, json_data):
        str_res = "[*] Virus Total report:\n"
        for scanner in json_data['scans']:
            str_res += "> " + scanner + " : [ Detected: " + str(json_data['scans'][scanner]['detected']) + " | Result: " + str(json_data['scans'][scanner]['result']) + " ]\n"
        return str_res + "Virus Total platform detects " + str(json_data['positives']) + " positive results for " + self.file_name + "\n[*] Virus total report end"



