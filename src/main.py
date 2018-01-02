import getopt
import sys

from src.analyzers.AGenerator import AGenerator
from src.reports.RGenerator import RGenerator
from src.utils.ConfigHelper import ConfigHelper
from src.utils.Constants import Constants
from src.utils.FileHelper import FileHelper


def main():
    #Get program arguments
    file_path = ""
    #By default applies all the analyzer
    analyzers = AGenerator.getAllAnalyzers()
    #By default generator a short report
    reports = RGenerator.getShortReport()
    reporting_level = Constants.SHORT_REPORTING
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hfao", ["help", "all", "file=", "output="])
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
            if arg == "medium":
                reports = RGenerator.getMediumReport()
                reporting_level = Constants.MEDIUM_REPORTING
            elif arg == "comprehensive":
                reports = RGenerator.getComprehensiveReport()
                reporting_level = Constants.COMPREHENSIVE_REPORTING
            else:
                if arg != "short":
                    assert False, "Error in output argument"
        else:
            assert False, "unhandled option"

    if not file_path:
        print("File is needed")
        sys.exit(2)

    #Setup params
    config_content = FileHelper.getConfigFile()
    setup_params = (ConfigHelper.getVirusTotalAPIKey(config_content), file_path)
    #Apply analyzers
    analyze_results = []
    for a in analyzers:
        a.setup(setup_params)
        a.analyze()
        analyze_results.append(a.report(reporting_level))

    #Generate results
    reports.generate(analyze_results)

if  __name__ =='__main__':main()