from abc import ABC


class IAnalyzer(ABC):

    @abstractmethod
    def setup(self, list):
        return NotImplemented

    @abstractmethod
    def analyze(self, file):
        return NotImplemented
