from os.path import basename


class FileHelper:

    def openFile(self, path):
        return open(path, 'rb')

    def getFileName(self, path):
        return basename(path)