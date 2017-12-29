import json
import time
from pip._vendor import requests

from src.Utils.FileHelper import FileHelper
from src.analyzers.IAnalyzer import IAnalyzer


class VirusTotal(IAnalyzer):

    def __init__(self):
        self.name = "Virus total analyzer"
        self.api_key = ""
        self.file_path = ""
        self.file_name = ""
        self.scan_id = ""

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
        response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params)
        try:
            self.scan_id = self.handleScanResponse(response)
        except Exception as error:
            print("Error when uploading file to virus total platform : " + repr(error))
        print("[*] File upload to Virus Total (scan id = " + self.scan_id + ")")
        #Retrieve scan result
        params = {'apikey': self.api_key, 'resource': self.scan_id}
        headers = {
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "gzip, Python"
        }
        while True:
            print("[*] Request Rapport (scan id = " + self.scan_id + ")")
            response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
                                    params=params, headers=headers)
            response_content = self.handleReportResponse(response)
            if response_content != 0:
                print("[!] Rapport received ")
                break
            time.sleep(30)
        print(response_content)
        #Parse results

    def handleScanResponse(self, response):
        json_data = response.json()
        if json_data['response_code'] != 1:
            raise Exception('Bad Response from Virus Total API')
        else:
            return json_data['scan_id']

    def handleReportResponse(self, response):
        json_data = response.json()
        if json_data['response_code'] != 1:
            return 0
        else:
            return json_data


