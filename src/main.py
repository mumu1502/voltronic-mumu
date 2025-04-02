#! /usr/bin/python3
import time
from voltronic import Voltronic
from mqtt import MQTT
import os

REPORT_INTERVAL_S = int(os.getenv('REPORT_INTERVAL_S', 1))

inverter = Voltronic()
client = MQTT()


def loop():
    while True:
        inverter.update("QMOD")
        inverter.update("QPIGS")
        inverter.update("QPIGS2")
        inverter.update("QPIWS")
        inverter.update("QLT")
        inverter.update("QET")
        inverter.update("QT")

        client.publish(inverter.sensors)
        time.sleep(REPORT_INTERVAL_S)


if __name__ == "__main__":
    loop()
