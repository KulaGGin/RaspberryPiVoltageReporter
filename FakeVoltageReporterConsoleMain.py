import platform
import random
import time
from FakeADS1115 import FakeADS1115
from CurrentReporter import CurrentReporter
from TransformerReportWebPage import *

def main():
    global currentReporter
    if platform.system() == "Windows":
        print("Running on Windows")
        voltageProvider = FakeADS1115()
        currentReporter = CurrentReporter(voltageProvider, TransformerReportWebPage)
    elif platform.system() == "Linux":
        print("Running on Linux")
        voltageProvider = FakeADS1115()
        currentReporter = CurrentReporter(voltageProvider, TransformerReportWebPage)
    while True:
        voltageProvider.P0Voltage = float(random.uniform(0, 5))
        voltageProvider.P1Voltage = float(random.uniform(0, 5))
        currentReporter.Report()
        time.sleep(10)

if __name__ == '__main__':
    main();
