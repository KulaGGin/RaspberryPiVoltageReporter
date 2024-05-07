import platform
import time
import tkinter as tk
from datetime import datetime
import random

from FakeVoltageProvider import FakeVoltageProvider
from VoltageReporter import VoltageReporter


TransformerReportWebPage = "http://37.229.48.234:8080/xwiki/bin/view/Transformer State Reporter/AddSensorReading"

StartFakeVoltageValueToReport = 11

window = tk.Tk()
window.title("Voltage Reporter")

ShouldReportReadings = False
voltageReporter = None
DateLabel2 = None

def reportVoltage():
    if ShouldReportReadings == False:
        return

    reportedVoltage = voltageReporter.ReportVoltage()
    DateLabel2.config(text=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    VoltageReadingLabel2.config(text=f"{reportedVoltage}V")
    window.after(1000, reportVoltage)

def onStartButtonClicked():
    global ShouldReportReadings
    ShouldReportReadings = True
    window.after(10000, reportVoltage)

def onStopButtonClicked():
    global ShouldReportReadings
    ShouldReportReadings = False


DateLabel1 = tk.Label(window, text="Last time values reported:")
DateLabel2 = tk.Label(window, text=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
DateLabel1.grid(row=1, column=0)
DateLabel2.grid(row=1, column=1)
StartButton = tk.Button(window, text="Start", command=onStartButtonClicked)
StopButton = tk.Button(window, text="Stop", command=onStopButtonClicked)
StartButton.grid(row=3, column=0)
StopButton.grid(row=3, column=1)

VoltageReadingLabel1 = tk.Label(window, text="Voltage Reading:")
VoltageReadingLabel2 = tk.Label(window, text="N/A")
VoltageReadingLabel1.grid(row=2, column=0)
VoltageReadingLabel2.grid(row=2, column=1)



def main():
    global voltageProvider
    global voltageReporter
    if platform.system() == "Windows":
        print("Running on Windows")
        voltageProvider = FakeVoltageProvider(StartFakeVoltageValueToReport)
        voltageReporter = VoltageReporter(voltageProvider, TransformerReportWebPage)
    elif platform.system() == "Linux":
        from RealVoltageProvider import RealVoltageProvider
        print("Running on Linux")
        voltageProvider = RealVoltageProvider()
        voltageReporter = VoltageReporter(voltageProvider, TransformerReportWebPage)

    while True:
        window.update()
        if platform.system() == "Windows":
            voltageProvider.SetVoltage(float(random.uniform(1, 5)))
if __name__ == '__main__':
    main()