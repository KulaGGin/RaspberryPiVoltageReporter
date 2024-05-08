from IADS1115 import IADS1115


class FakeADS1115(IADS1115):
    def __init__(self, P0StartingVoltage = 0, P1StartingVoltage = 0, P2StartingVoltage = 0, P3StartingVoltage = 0):
        self.P0Voltage = P0StartingVoltage
        self.P1Voltage = P1StartingVoltage
        self.P2Voltage = P2StartingVoltage
        self.P3Voltage = P3StartingVoltage

    def GetVoltageP0(self):
        return self.P0Voltage

    def GetVoltageP1(self):
        return self.P1Voltage

    def GetVoltageP2(self):
        return self.P2Voltage

    def GetVoltageP3(self):
        return self.P3Voltage
