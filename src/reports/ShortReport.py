from abc import abstractmethod

from src.reports.IReport import IReport
from src.utils.Constants import Constants


class ShortReport(IReport):

    #Input is a tuple list with (analyzer, result)
    #result is a boolean
    #Display the investigation result only
    def generate(self, dict):
        print(Constants.COMMON_INVESTIGATION_REPORT)
        triggered = False
        for tuple in dict:
            if tuple[1]:
                triggered = True
                break
        if triggered:
            print(Constants.COMMON_MALICIOUS_MESSAGE)
        else:
            print(Constants.COMMON_CLEAN_MESSAGE)
        print(Constants.COMMON_INVESTIGATION_REPORT)