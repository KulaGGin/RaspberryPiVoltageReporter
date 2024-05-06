from numpy import interp
import board
import time
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

from VoltageProvider import VoltageProvider

class RealVoltageProvider(VoltageProvider):
    def __init__(self):
        # Initialize the I2C interface
        self.i2c = busio.I2C(board.SCL, board.SDA)

        # Create an ADS1115 object
        self.ads = ADS.ADS1115(self.i2c)

        # Define the analog input channel
        self.channel = AnalogIn(self.ads, ADS.P0)

        self.voltageSensorInputVoltageMinMax = [0, 25]
        self.voltageSensorOutputVoltageMinMax = [0, 5]

    def GetVoltage(self):
        adsVoltageReading = self.channel.voltage;
        actualVoltage = interp(adsVoltageReading, self.voltageSensorInputVoltageMinMax, self.voltageSensorOutputVoltageMinMax)
        print("ADS Analog Value: ", self.channel.value, "ADS Voltage: ", adsVoltageReading)
        print("Actual Voltage: ", actualVoltage)
        return self.channel.voltage
