from FakeVoltageProvider import FakeVoltageProvider
import requests

class VoltageReporter():
    def __init__(self, fakeVoltageProvider, url):
        self.url = url
        self.VoltageProvider = fakeVoltageProvider

    def ReportVoltage(self):
        voltage = self.VoltageProvider.GetVoltage()
        voltage = round(voltage, 2)
        recording = {'reading': voltage, 'xpage': 'plain', 'outputSyntax': 'plain'}
        response = requests.get(self.url, params=recording, verify=True)
        print(f"Made a request to page: {self.url}")
        print(f"Response code is: {response}")
        print(f"Response content is: {response.text}")
        print(f"Tried to push current with value: {voltage}")
        return voltage

    def SetVoltageProvider(self, voltageProvider):
        self.VoltageProvider = voltageProvider