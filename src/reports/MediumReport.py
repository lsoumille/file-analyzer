from src.reports.IReport import IReport
from src.utils.Constants import Constants


class MediumReport(IReport):

    # Input is a tuple list with (analyzer, result)
    # result is a boolean
    def generate(self, dict):
        print(Constants.COMMON_INVESTIGATION_REPORT)
        is_malicious = False
        triggered = 0
        for tuple in dict:
            if tuple[1] == '':
                print("[*] " + tuple[0] + " result not found")
            elif tuple[1]:
                print("[!] " + tuple[0] + " detected malicious content")
                is_malicious = True
                triggered = triggered + 1
            else:
                print("[*] " + tuple[0] + " says the file is safe")
        if is_malicious:
            print(Constants.COMMON_MALICIOUS_MESSAGE)
            print("Signature triggered from " + str(triggered) + " analyzers")
        else:
            print(Constants.COMMON_CLEAN_MESSAGE)
        print(Constants.COMMON_INVESTIGATION_REPORT)