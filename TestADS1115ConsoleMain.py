from numpy import interp
import board
import time
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from SensorsConfiguration import *

# Initialize the I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# Create an ADS1115 object
ads = ADS.ADS1115(i2c)

# Define the analog input channel
VoltageSensorChannel = AnalogIn(ads, ADS.P0)
CurrentSensorChannel = AnalogIn(ads, ADS.P1)

# Loop to read the analog input continuously
while True:
    actualVoltage = interp(VoltageSensorChannel.voltage, VoltageSensorOutputVoltageMinMax, VoltageSensorInputVoltageMinMax)
    actualCurrent = interp(CurrentSensorChannel.voltage, CurrentSensorOutputCurrentMinMax, CurrentSensorInputCurrentMinMax)

    print("ADS A0 value: ", VoltageSensorChannel.value, "ADS A0 voltage: ", VoltageSensorChannel.voltage)
    print("ADS A1 value: ", CurrentSensorChannel.value, "ADS A1 voltage: ", CurrentSensorChannel.voltage)
    print("Actual Voltage: ", actualVoltage)
    print("Actual Current: ", actualCurrent)
    time.sleep(5)