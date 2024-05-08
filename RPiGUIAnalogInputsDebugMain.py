from numpy import interp
import platform
import time
import tkinter as tk
from datetime import datetime
import random

from FakeADS1115 import FakeADS1115

TransformerReportWebPage = "http://37.229.48.234:8080/xwiki/bin/view/Transformer State Reporter/AddSensorReading"

StartFakeVoltageValueToReport = 11

window = tk.Tk()
window.title("Voltage Reporter")

ShouldReportReadings = False
DateLabel2 = None

voltageSensorInputVoltageMinMax = [0, 25]
voltageSensorOutputVoltageMinMax = [0, 5]

currentSensorInputCurrentMinMax = [0, 200]
currentSensorOutputCurrentMinMax = [0, 5]

def reportVoltage():
    if ShouldReportReadings == False:
        return

    DateLabel2.config(text=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

    P0Voltage = voltageProvider.GetVoltageP0()
    P1Voltage = voltageProvider.GetVoltageP1()
    P2Voltage = voltageProvider.GetVoltageP1()
    P3Voltage = voltageProvider.GetVoltageP1()

    actualVoltage = interp(P0Voltage, voltageSensorOutputVoltageMinMax, voltageSensorInputVoltageMinMax)
    actualCurrent = interp(P1Voltage, currentSensorOutputCurrentMinMax, currentSensorInputCurrentMinMax)

    P0VoltageReadingLabel2.config(text=f"{round(P0Voltage, 2)}V")
    P1VoltageReadingLabel2.config(text=f"{round(P1Voltage, 2)}V")
    P2VoltageReadingLabel2.config(text=f"{round(P2Voltage, 2)}V")
    P3VoltageReadingLabel2.config(text=f"{round(P3Voltage, 2)}V")

    ActualVoltageLabel2.config(text=f"{round(actualVoltage, 2)}V")
    ActualCurrentLabel2.config(text=f"{round(actualCurrent, 2)}A")

    window.after(1000, reportVoltage)

def onStartButtonClicked():
    global ShouldReportReadings
    ShouldReportReadings = True
    window.after(1000, reportVoltage)

def onStopButtonClicked():
    global ShouldReportReadings
    ShouldReportReadings = False


DateLabel1 = tk.Label(window, text="Last time values reported:")
DateLabel2 = tk.Label(window, text=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
DateLabel1.grid(row=1, column=0)
DateLabel2.grid(row=1, column=1)
StartButton = tk.Button(window, text="Start", command=onStartButtonClicked)
StopButton = tk.Button(window, text="Stop", command=onStopButtonClicked)

P0VoltageReadingLabel1 = tk.Label(window, text="Voltage P0 Reading:")
P0VoltageReadingLabel2 = tk.Label(window, text="N/A")
P0VoltageReadingLabel1.grid(row=2, column=0)
P0VoltageReadingLabel2.grid(row=2, column=1)

P1VoltageReadingLabel1 = tk.Label(window, text="Voltage P1 Reading:")
P1VoltageReadingLabel2 = tk.Label(window, text="N/A")
P1VoltageReadingLabel1.grid(row=3, column=0)
P1VoltageReadingLabel2.grid(row=3, column=1)

P2VoltageReadingLabel1 = tk.Label(window, text="Voltage P2 Reading:")
P2VoltageReadingLabel2 = tk.Label(window, text="N/A")
P2VoltageReadingLabel1.grid(row=4, column=0)
P2VoltageReadingLabel2.grid(row=4, column=1)

P3VoltageReadingLabel1 = tk.Label(window, text="Voltage P3 Reading:")
P3VoltageReadingLabel2 = tk.Label(window, text="N/A")
P3VoltageReadingLabel1.grid(row=5, column=0)
P3VoltageReadingLabel2.grid(row=5, column=1)

ActualVoltageLabel1 = tk.Label(window, text="Actual Voltage on A0:")
ActualVoltageLabel2 = tk.Label(window, text="N/A")
ActualVoltageLabel1.grid(row=6, column=0)
ActualVoltageLabel2.grid(row=6, column=1)

ActualCurrentLabel1 = tk.Label(window, text="Actual Current on A1:")
ActualCurrentLabel2 = tk.Label(window, text="N/A")
ActualCurrentLabel1.grid(row=7, column=0)
ActualCurrentLabel2.grid(row=7, column=1)

StartButton.grid(row=8, column=0)
StopButton.grid(row=8, column=1)

def main():
    global voltageProvider
    if platform.system() == "Windows":
        print("Running on Windows")
        voltageProvider = FakeADS1115()
    elif platform.system() == "Linux":
        from RealADS1115 import RealADS1115
        print("Running on Linux")
        voltageProvider = RealADS1115()
    while True:
        window.update()
        if platform.system() == "Windows":
            voltageProvider.P0Voltage = float(random.uniform(0, 5))
            voltageProvider.P1Voltage = float(random.uniform(0, 5))
            voltageProvider.P2Voltage = float(random.uniform(0, 5))
            voltageProvider.P3Voltage = float(random.uniform(0, 5))
if __name__ == '__main__':
    main()