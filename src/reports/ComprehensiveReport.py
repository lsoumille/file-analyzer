from src.reports.IReport import IReport
from src.utils.Constants import Constants


class ComprehensiveReport(IReport):

    # Input is a tuple list with (analyzer, result, content)
    # result is a boolean
    def generate(self, dict):
        print(Constants.COMMON_INVESTIGATION_REPORT)
        is_malicious = False
        triggered = 0
        for tuple in dict:
            if tuple[1] == '':
                print("[*] " + tuple[0] + " result not found")
                continue
            elif tuple[1]:
                print("[!] " + tuple[0] + " detected malicious content")
                is_malicious = True
                triggered = triggered + 1
            else:
                print("[*] " + tuple[0] + " says the file is safe")
            #Print result details
            if tuple[2]:
                print(tuple[2])
        if is_malicious:
            print(Constants.COMMON_MALICIOUS_MESSAGE)
            print("Signature triggered from " + str(triggered) + " analyzers")
        else:
            print(Constants.COMMON_CLEAN_MESSAGE)
        print(Constants.COMMON_INVESTIGATION_REPORT)