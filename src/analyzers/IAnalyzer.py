from abc import ABC, abstractmethod


class IAnalyzer(ABC):

    @abstractmethod
    def setup(self, list):
        return NotImplemented

    @abstractmethod
    def analyze(self):
        return NotImplemented
