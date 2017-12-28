import json
import time
from pip._vendor import requests
from src.Utils import FileHelper
from src.analyzers.IAnalyzer import IAnalyzer


class VirusTotal(IAnalyzer):

    def __init__(self):
        self.name = "Virus total analyzer"
        self.api_key = ""
        self.file_path = ""
        self.file_name = ""
        self.scan_id = ""

    def setup(self, list):
        if list[0]:
            self.api_key = list[0]
        if list[1]:
            self.file_path = list[1]


    def analyze(self, file):
        fh = FileHelper()
        self.file_name = fh.getFileName(self.file_path)
        params = {'apikey': self.api_key}
        files = {'file': (self.file_name, fh.openFile(self.file_path))}
        response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params)
        try:
            self.scan_id = self.handleScanResponse(response)
        except Exception as error:
            print("Error when uploading file to virus total platform : " + repr(error))

        #Retrieve scan result
        params = {'apikey': self.api_key, 'resource': self.scan_id}
        headers = {
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "gzip, Python"
        }
        while True:
            response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
                                    params=params, headers=headers)
            response_content = self.handleReportResponse(response)
            if response_content == 0:
                break
            time.sleep(15)
        print(response_content)
        #Parse results

    def handleScanResponse(self, response):
        json_data = json.loads(response)
        if json_data['response_code'] != 1:
            raise Exception('Bad Response from Virus Total API')
        else:
            return json_data['scan_id']

    def handleReportResponse(self, response):
        json_data = json.loads(response)
        if json_data['response_code'] != 1:
            return 0
        else:
            return json_data


