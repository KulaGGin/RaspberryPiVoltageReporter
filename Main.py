import platform
import time
from FakeVoltageProvider import FakeVoltageProvider
from VoltageReporter import VoltageReporter

TransformerReportWebPage = "http://37.229.48.234:8080/xwiki/bin/view/Transformer State Reporter/AddSensorReading"

FakeVoltageValueToReport = 11

def main():
    global voltageProvider
    if platform.system() == "Windows":
        voltageProvider = FakeVoltageProvider(FakeVoltageValueToReport)
        voltageReporter = VoltageReporter(voltageProvider, TransformerReportWebPage)
    elif platform.system() == "Linux":
        voltageProvider = FakeVoltageProvider(FakeVoltageValueToReport)
        voltageReporter = VoltageReporter(voltageProvider, TransformerReportWebPage)
    while True:
        voltageReporter.ReportVoltage()
        time.sleep(10)

if __name__ == '__main__':
    main();
