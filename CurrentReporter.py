import requests
from numpy import interp

class CurrentReporter():
    def __init__(self, ADS1115, url):
        self.url = url
        self.ADS1115 = ADS1115
        self.VoltageSensorInputCurrentMinMax = [0, 25]
        self.VoltageSensorOutputCurrentMinMax = [0, 5]
        self.CurrentSensorInputCurrentMinMax = [0, 200]
        self.CurrentSensorOutputCurrentMinMax = [0, 5]
    def Report(self):
        rawADSVoltageReading = self.ADS1115.GetVoltageP0()
        actualVoltage = interp(rawADSVoltageReading, self.VoltageSensorOutputCurrentMinMax, self.VoltageSensorInputCurrentMinMax)
        actualVoltage = round(actualVoltage, 2)

        rawADSCurrentReading = self.ADS1115.GetVoltageP1()
        actualCurrent = interp(rawADSCurrentReading, self.CurrentSensorOutputCurrentMinMax, self.CurrentSensorInputCurrentMinMax)
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