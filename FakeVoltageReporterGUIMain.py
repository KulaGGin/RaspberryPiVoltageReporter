import platform
import time
import tkinter as tk
from datetime import datetime

from numpy.core.defchararray import isnumeric

from FakeADS1115 import FakeADS1115
from CurrentReporter import CurrentReporter
import random

TransformerReportWebPage = "http://37.229.48.234:8080/xwiki/bin/view/Transformer State Reporter/AddSensorReading"

StartFakeVoltageValueToReport = 1.5
StartFakeCurrentValueToReport = 2.6

window = tk.Tk()
window.title("Fake Voltage Reporter")

VoltageLabel = tk.Label(window, text="Voltage to send:")
VoltageEntry = tk.Entry(window, width=16)
VoltageEntry.insert(0, StartFakeVoltageValueToReport)
VoltageLabel.grid(row=0, column=0)   # grid dynamically divides the space in a grid
VoltageEntry.grid(row=0, column=1)   # and arranges widgets accordingly

CurrentLabel = tk.Label(window, text="Current to send:")
CurrentEntry = tk.Entry(window, width=16)
CurrentEntry.insert(0, StartFakeCurrentValueToReport)
CurrentLabel.grid(row=1, column=0)   # grid dynamically divides the space in a grid
CurrentEntry.grid(row=1, column=1)   # and arranges widgets accordingly



ShouldReportReadings = False
currentReporter = None
DateLabel2 = None

def reportVoltage():
    if ShouldReportReadings == False:
        return

    (voltage, current) = currentReporter.Report()
    DateLabel2.config(text=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
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
DateLabel1.grid(row=2, column=0)
DateLabel2.grid(row=2, column=1)
StartButton = tk.Button(window, text="Start", command=onStartButtonClicked)
StopButton = tk.Button(window, text="Stop", command=onStopButtonClicked)
StartButton.grid(row=3, column=0)
StopButton.grid(row=3, column=1)



def main():
    global ADS1115
    global currentReporter
    if platform.system() == "Windows":
        ADS1115 = FakeADS1115(StartFakeVoltageValueToReport, StartFakeCurrentValueToReport)
        currentReporter = CurrentReporter(ADS1115, TransformerReportWebPage)
    elif platform.system() == "Linux":
        ADS1115 = FakeADS1115(StartFakeVoltageValueToReport, StartFakeCurrentValueToReport)
        currentReporter = CurrentReporter(ADS1115, TransformerReportWebPage)

    while True:
        window.update()
        newFakeVoltage = VoltageEntry.get()
        newFakeCurrent = CurrentEntry.get()

        try:
            float(newFakeVoltage)
        except ValueError:
            return
        try:
            float(newFakeCurrent)
        except ValueError:
            return

        ADS1115.P0Voltage = float(newFakeVoltage)
        ADS1115.P1Voltage = float(newFakeCurrent)

if __name__ == '__main__':
    main()