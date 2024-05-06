import platform
import time
from FakeVoltageProvider import FakeVoltageProvider
from VoltageReporter import VoltageReporter

TransformerReportWebPage = "http://37.229.48.234:8080/xwiki/bin/view/Transformer State Reporter/AddSensorReading"

FakeVoltageValueToReport = 11

def main():
    if platform.system() == "Windows":
        fakeVoltageProvider = FakeVoltageProvider(FakeVoltageValueToReport)
        voltageReporter = VoltageReporter(fakeVoltageProvider, TransformerReportWebPage)
    elif platform.system() == "Linux":
        fakeVoltageProvider = FakeVoltageProvider(FakeVoltageValueToReport)
        voltageReporter = VoltageReporter(fakeVoltageProvider, TransformerReportWebPage)

    while True:
        voltageReporter.ReportVoltage()
        time.sleep(1)

if __name__ == '__main__':
    main();
