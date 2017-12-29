import getopt
import sys

from src.analyzers.AGenerator import AGenerator
from src.analyzers.VirusTotal import VirusTotal
from src.reports.RGenerator import RGenerator
from src.reports.ShortReport import ShortReport
from src.utils.Constants import Constants


def main():
    #Step 1: Get program arguments
    file_path = ""
    #By default applies all the analyzer
    analyzers = AGenerator.getAllAnalyzers()
    #By default generator a short report
    reports = RGenerator.getShortReport()
    reporting_level = Constants.SHORT_REPORTING
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hfao", ["help", "all", "file=", "output"])
    except getopt.GetoptError:
        #usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            #usage()
            sys.exit()
        elif opt in ("-f", "--file"):
            file_path = arg
        elif opt in ("-a," "--all"):
            analyzers = AGenerator.getAllAnalyzers()
        elif opt in ("-o", "--output"):
            print("TMP")
            #Handle report argument
        else:
            assert False, "unhandled option"

    if not file_path:
        print("File is needed")
        sys.exit(2)

    #Setup params
    setup_params = ('', file_path)
    #Apply analyzers
    analyze_results = []
    for a in analyzers:
        a.setup(setup_params)
        a.analyze()
        analyze_results.append(a.report(reporting_level))

    #Generate results
    reports.generate(analyze_results)

    ###DEBUG###
    #analyzer = VirusTotal()
    #report = ShortReport()
    #setup_params = ('', file_path)
    #analyzer.setup(setup_params)
    #response_tuple = analyzer.analyze()
    #response_dict = dict([response_tuple])
    #report.generate(response_dict)




if  __name__ =='__main__':main()