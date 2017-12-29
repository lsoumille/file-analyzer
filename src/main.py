import getopt
import sys


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



if  __name__ =='__main__':main()