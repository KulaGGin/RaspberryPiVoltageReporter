from numpy import interp
import board
import time
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Initialize the I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# Create an ADS1115 object
ads = ADS.ADS1115(i2c)

# Define the analog input channel
channel = AnalogIn(ads, ADS.P0)

voltageSensorInputVoltageMinMax = [0, 25]
voltageSensorOutputVoltageMinMax = [0, 5]

# Loop to read the analog input continuously
while True:
    adsVoltageReading = channel.voltage;
    actualVoltage = interp(adsVoltageReading, voltageSensorInputVoltageMinMax, voltageSensorOutputVoltageMinMax)
    print("ADS analog value: ", channel.value, "AFS input voltage: ", channel.voltage)
    print("Actual Voltage: ", actualVoltage)
    time.sleep(0.2)