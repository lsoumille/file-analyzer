from pip._vendor.requests.packages import urllib3

from src.analyzers.IAnalyzer import IAnalyzer
from src.utils.Constants import Constants
from src.utils.FileHelper import FileHelper


class MetadefenderCloud(IAnalyzer):

    def __init__(self):
        self.name = "Metadefender Cloud analyzer"
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
        file_content = fh.openFile(self.file_path)
        request = urllib3.Request(Constants.METADEFENDER_SENDING_URL, file_content)
        request.add_header('apikey', self.api_key)
        request.add_header('filename', self.file_name)
        response = request.post()
        try:
            self.scan_id = self.handleScanResponse(response)
        except Exception as error:
            print("Error when uploading file to Metadefender Cloud platform : " + repr(error))
            return
        print("[*] File upload to Metadefender Cloud (scan id = " + self.scan_id + ")")

    def report(self, level):
        print("TODO")