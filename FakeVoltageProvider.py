from VoltageProvider import VoltageProvider


class FakeVoltageProvider(VoltageProvider):
    def __init__(self, valueToReturn):
        self.ValueToReturn = valueToReturn

    def GetVoltage(self):
        return self.ValueToReturn
