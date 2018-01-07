from src.analyzers.MetadefenderCloud import MetadefenderCloud
from src.analyzers.VirusTotal import VirusTotal


class AGenerator:
    @staticmethod
    def getAllAnalyzers():
        return [VirusTotal(), MetadefenderCloud()]

    def getVirusTotalAnalyzer(self):
        return VirusTotal()

    def getMetadefenderAnalyzer(self):
        return MetadefenderCloud()