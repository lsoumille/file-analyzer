from abc import ABC, abstractmethod


class IAnalyzer(ABC):

    @abstractmethod
    def setup(self, tuple):
        return NotImplemented

    @abstractmethod
    def analyze(self):
        return NotImplemented

    @abstractmethod
    def report(self, level):
        return NotImplemented
