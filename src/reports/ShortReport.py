from abc import abstractmethod

from src.reports.IReport import IReport
from src.utils.Constants import Constants


class ShortReport(IReport):

    def generate(self, dict):
        for tuple in dict:
            if tuple[1] == True:
                print("### Malicious content detected ###")
                return
        print(Constants.COMMON_CLEAN_MESSAGE)