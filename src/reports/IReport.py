from abc import ABC, abstractmethod


class IReport(ABC):

    @abstractmethod
    def generate(self, dict):
        return NotImplemented
