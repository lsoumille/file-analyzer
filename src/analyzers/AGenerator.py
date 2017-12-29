from src.analyzers.VirusTotal import VirusTotal


class AGenerator:
    @staticmethod
    def getAllAnalyzers():
        return [VirusTotal()]

    def getVirusTotalAnalyzer(self):
        return VirusTotal()