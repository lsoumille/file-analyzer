import getopt
import sys

from src.analyzers.VirusTotal import VirusTotal
from src.reports.ShortReport import ShortReport


def main():
    file_path = ""
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf", ["help", "file="])
    except getopt.GetoptError:
        #usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            #usage()
            sys.exit()
        elif opt in ("-f", "--file"):
            file_path = arg
        else:
            assert False, "unhandled option"

    if not file_path:
        print("File is needed")
        sys.exit(2)

    analyzer = VirusTotal()
    report = ShortReport()
    setup_params = ('', file_path)
    analyzer.setup(setup_params)
    response_tuple = analyzer.analyze()
    response_dict = dict([response_tuple])
    report.generate(response_dict)




if  __name__ =='__main__':main()