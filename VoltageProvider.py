from abc import ABC, abstractmethod


class VoltageProvider(ABC):
    @abstractmethod
    def GetVoltage(self):
        return 0.1