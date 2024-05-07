import platform
import time
import tkinter as tk
from datetime import datetime

from numpy.core.defchararray import isnumeric

from FakeVoltageProvider import FakeVoltageProvider
from VoltageReporter import VoltageReporter


TransformerReportWebPage = "http://37.229.48.234:8080/xwiki/bin/view/Transformer State Reporter/AddSensorReading"

StartFakeVoltageValueToReport = 11

window = tk.Tk()
window.title("Fake Voltage Reporter")

VoltageLabel = tk.Label(window, text="Voltage to send:")

VoltageEntry = tk.Entry(window, width=16)
VoltageLabel.grid(row=0, column=0)   # grid dynamically divides the space in a grid
VoltageEntry.grid(row=0, column=1)   # and arranges widgets accordingly

ShouldReportReadings = False
voltageReporter = None
DateLabel2 = None

def reportVoltage():
    if ShouldReportReadings == False:
        return

    voltageReporter.ReportVoltage()
    DateLabel2.config(text=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    window.after(1000, reportVoltage)
def onStartButtonClicked():
    global ShouldReportReadings
    ShouldReportReadings = True
    window.after(1000, reportVoltage)

def onStopButtonClicked():
    global ShouldReportReadings
    ShouldReportReadings = False


VoltageEntry.insert(0, StartFakeVoltageValueToReport)
DateLabel1 = tk.Label(window, text="Last time values reported:")
DateLabel2 = tk.Label(window, text=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
DateLabel1.grid(row=1, column=0)
DateLabel2.grid(row=1, column=1)
StartButton = tk.Button(window, text="Start", command=onStartButtonClicked)
StopButton = tk.Button(window, text="Stop", command=onStopButtonClicked)
StartButton.grid(row=2, column=0)
StopButton.grid(row=2, column=1)



def main():
    global fakeVoltageProvider
    global voltageReporter
    if platform.system() == "Windows":
        fakeVoltageProvider = FakeVoltageProvider(StartFakeVoltageValueToReport)
        voltageReporter = VoltageReporter(fakeVoltageProvider, TransformerReportWebPage)
    elif platform.system() == "Linux":
        fakeVoltageProvider = FakeVoltageProvider(StartFakeVoltageValueToReport)
        voltageReporter = VoltageReporter(fakeVoltageProvider, TransformerReportWebPage)

    while True:
        window.update()
        newFakeValue = VoltageEntry.get()

        try:
            float(newFakeValue)
        except ValueError:
            return

        fakeVoltageProvider.SetVoltage(float(newFakeValue))

if __name__ == '__main__':
    main()