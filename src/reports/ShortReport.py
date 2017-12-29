from abc import abstractmethod

from src.reports.IReport import IReport
from src.utils.Constants import Constants


class ShortReport(IReport):

    def generate(self, dict):
        for key, value in dict.items():
            if value == True:
                print("### Malicious content detected ###")
                return
        print(Constants.COMMON_CLEAN_MESSAGE)