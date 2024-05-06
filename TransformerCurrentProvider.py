from abc import ABC, abstractmethod


class TransformerCurrentProvider(ABC):
    @abstractmethod
    def GetCurrent(self):
        return 0.1