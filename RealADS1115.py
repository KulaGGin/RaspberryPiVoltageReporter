from numpy import interp
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

from IADS1115 import IADS1115

class RealADS1115(IADS1115):
    def __init__(self):
        # Initialize the I2C interface
        self.i2c = busio.I2C(board.SCL, board.SDA)

        # Create an ADS1115 object
        self.ads = ADS.ADS1115(self.i2c)

        # Define the analog input channel
        self.P0Channel = AnalogIn(self.ads, ADS.P0)
        self.P1Channel = AnalogIn(self.ads, ADS.P1)
        self.P2Channel = AnalogIn(self.ads, ADS.P2)
        self.P3Channel = AnalogIn(self.ads, ADS.P3)

        self.voltageSensorInputVoltageMinMax = [0, 25]
        self.voltageSensorOutputVoltageMinMax = [0, 5]

    def GetVoltageP0(self):
        adsVoltageReading = self.P0Channel.voltage;
        return adsVoltageReading

    def GetVoltageP1(self):
        adsVoltageReading = self.P1Channel.voltage;
        return adsVoltageReading

    def GetVoltageP2(self):
        adsVoltageReading = self.P2Channel.voltage;
        return adsVoltageReading

    def GetVoltageP3(self):
        adsVoltageReading = self.P3Channel.voltage;
        return adsVoltageReading
