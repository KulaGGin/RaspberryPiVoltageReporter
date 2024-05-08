import platform
import time
from FakeADS1115 import FakeADS1115
from CurrentReporter import CurrentReporter

TransformerReportWebPage = "http://37.229.48.234:8080/xwiki/bin/view/Transformer State Reporter/AddSensorReading"

FakeVoltageValueToReport = 4.3

def main():
    global currentReporter
    if platform.system() == "Windows":
        print("Running on Windows")
        voltageProvider = FakeADS1115(FakeVoltageValueToReport)
        currentReporter = CurrentReporter(voltageProvider, TransformerReportWebPage)
    elif platform.system() == "Linux":
        print("Running on Linux")
        voltageProvider = FakeADS1115(FakeVoltageValueToReport)
        currentReporter = CurrentReporter(voltageProvider, TransformerReportWebPage)
    while True:
        currentReporter.Report()

        time.sleep(10)

if __name__ == '__main__':
    main();
