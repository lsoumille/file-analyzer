from os.path import basename

import yaml

from src.utils.Constants import Constants


class FileHelper:

    def openFile(self, path):
        return open(path, 'rb')

    def getFileName(self, path):
        return basename(path)

    @staticmethod
    def getConfigFile():
        return yaml.load(open(Constants.CONFIG_PATH, 'r'))