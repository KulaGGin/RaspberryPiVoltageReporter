from abc import ABC, abstractmethod


class IADS1115(ABC):
    @abstractmethod
    def GetVoltageP0(self):
        return 0.1

    @abstractmethod
    def GetVoltageP1(self):
        return 0.1

    @abstractmethod
    def GetVoltageP2(self):
        return 0.1

    @abstractmethod
    def GetVoltageP3(self):
        return 0.1