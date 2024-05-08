import requests
from numpy import interp
from SensorsConfiguration import *

class CurrentReporter():
    def __init__(self, ADS1115, url):
        self.url = url
        self.ADS1115 = ADS1115

    def Report(self):
        rawADSVoltageReading = self.ADS1115.GetVoltageP0()
        actualVoltage = interp(rawADSVoltageReading, VoltageSensorOutputVoltageMinMax, VoltageSensorInputVoltageMinMax)
        actualVoltage = round(actualVoltage, 2)

        rawADSCurrentReading = self.ADS1115.GetVoltageP1()
        actualCurrent = interp(rawADSCurrentReading, CurrentSensorOutputCurrentMinMax, CurrentSensorInputCurrentMinMax)
        actualCurrent = round(actualCurrent, 2)
        recording = {'voltage': actualVoltage, 'current': actualCurrent, 'reading': actualVoltage, 'xpage': 'plain', 'outputSyntax': 'plain'}
        print(recording)
        response = requests.get(self.url, params=recording, verify=True)
        print(f"Made a request to page: {self.url}")
        print(f"Response code is: {response}")
        print(f"Response content is: {response.text}")
        print(f"Tried to push current with value: {actualVoltage}")

        return (actualVoltage, actualCurrent)

    def SetVoltageProvider(self, voltageProvider):
        self.ADS1115 = voltageProvider