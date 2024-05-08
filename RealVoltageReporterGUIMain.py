import platform
import time
import tkinter as tk
from datetime import datetime
import random

from FakeADS1115 import FakeADS1115
from CurrentReporter import CurrentReporter


TransformerReportWebPage = "http://37.229.48.234:8080/xwiki/bin/view/Transformer State Reporter/AddSensorReading"

window = tk.Tk()
window.title("Voltage Reporter")

ShouldReportReadings = False
currentReporter = None
DateLabel2 = None

def reportVoltage():
    if ShouldReportReadings == False:
        return

    (reportedVoltage, reportedCurrent) = currentReporter.Report()
    DateLabel2.config(text=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    ActualVoltageLabel2.config(text=f"{reportedVoltage}V")
    ActualCurrentLabel2.config(text=f"{reportedCurrent}A")
    window.after(10000, reportVoltage)

def onStartButtonClicked():
    global ShouldReportReadings
    ShouldReportReadings = True
    reportVoltage()

def onStopButtonClicked():
    global ShouldReportReadings
    ShouldReportReadings = False


DateLabel1 = tk.Label(window, text="Last time values reported:")
DateLabel2 = tk.Label(window, text=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
DateLabel1.grid(row=1, column=0)
DateLabel2.grid(row=1, column=1)
StartButton = tk.Button(window, text="Start", command=onStartButtonClicked)
StopButton = tk.Button(window, text="Stop", command=onStopButtonClicked)

ActualVoltageLabel1 = tk.Label(window, text="Voltage Reading:")
ActualVoltageLabel2 = tk.Label(window, text="N/A")
ActualVoltageLabel1.grid(row=2, column=0)
ActualVoltageLabel2.grid(row=2, column=1)

ActualCurrentLabel1 = tk.Label(window, text="Current Reading:")
ActualCurrentLabel2 = tk.Label(window, text="N/A")
ActualCurrentLabel1.grid(row=3, column=0)
ActualCurrentLabel2.grid(row=3, column=1)

StartButton.grid(row=4, column=0)
StopButton.grid(row=4, column=1)


def main():
    global voltageProvider
    global currentReporter
    if platform.system() == "Windows":
        print("Running on Windows")
        voltageProvider = FakeADS1115()
        currentReporter = CurrentReporter(voltageProvider, TransformerReportWebPage)
    elif platform.system() == "Linux":
        from RealADS1115 import RealADS1115
        print("Running on Linux")
        voltageProvider = RealADS1115()
        currentReporter = CurrentReporter(voltageProvider, TransformerReportWebPage)

    while True:
        if platform.system() == "Windows":
            voltageProvider.P0Voltage = float(random.uniform(0, 5))
            voltageProvider.P1Voltage = float(random.uniform(0, 5))
            voltageProvider.P2Voltage = float(random.uniform(0, 5))
            voltageProvider.P3Voltage = float(random.uniform(0, 5))

        window.update()

if __name__ == '__main__':
    main()