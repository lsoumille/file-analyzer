from src.reports.MediumReport import MediumReport
from src.reports.ShortReport import ShortReport


class RGenerator:

    @staticmethod
    def getShortReport():
        return ShortReport()

    @staticmethod
    def getMediumReport():
        return MediumReport()


