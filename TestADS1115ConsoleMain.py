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
VoltageSensorChannel = AnalogIn(ads, ADS.P0)
CurrentSensorChannel = AnalogIn(ads, ADS.P1)

voltageSensorInputVoltageMinMax = [0, 25]
voltageSensorOutputVoltageMinMax = [0, 5]

currentSensorInputCurrentMinMax = [0, 200]
currentSensorOutputCurrentMinMax = [0, 5]

# Loop to read the analog input continuously
while True:
    actualVoltage = interp(VoltageSensorChannel.voltage, voltageSensorOutputVoltageMinMax, voltageSensorInputVoltageMinMax)
    actualCurrent = interp(CurrentSensorChannel.voltage, currentSensorOutputCurrentMinMax, currentSensorInputCurrentMinMax)

    print("ADS A0 value: ", VoltageSensorChannel.value, "ADS A0 voltage: ", VoltageSensorChannel.voltage)
    print("ADS A1 value: ", CurrentSensorChannel.value, "ADS A1 voltage: ", CurrentSensorChannel.voltage)
    print("Actual Voltage: ", actualVoltage)
    print("Actual Current: ", actualCurrent)
    time.sleep(0.2)