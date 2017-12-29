import getopt
import sys

from src.analyzers.VirusTotal import VirusTotal


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
    setup_params = ('86cfb1aa15979e6f0a97725fe3c56e03b94ed32800a2bfd080c6b72dae6e37da', file_path)
    analyzer.setup(setup_params)
    analyzer.analyze()



if  __name__ =='__main__':main()