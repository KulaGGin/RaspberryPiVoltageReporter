import platform
import time
from FakeTransformerCurrentProvider import FakeTransformerCurrentProvider
from TransformerCurrentReporter import TransformerCurrentReporter

TransformerReportWebPage = "http://desktop-pcqmqk8:8080/xwiki/bin/view/Transformer State Reporter/AddSensorReading"

def main():
    if platform.system() == "Windows":
        fakeTransformerCurrentProvider = FakeTransformerCurrentProvider()
        transformerCurrentReporter = TransformerCurrentReporter(fakeTransformerCurrentProvider, TransformerReportWebPage)
    elif platform.system() == "Linux":
        fakeTransformerCurrentProvider = FakeTransformerCurrentProvider()
        transformerCurrentReporter = TransformerCurrentReporter(fakeTransformerCurrentProvider, TransformerReportWebPage)

    while True:
        transformerCurrentReporter.ReportCurrent()
        time.sleep(1)

if __name__ == '__main__':
    main();
