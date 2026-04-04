import os, sys, io
import M5
from M5 import *
import time
from unit import EarthUnit

MOISTURE_CUT_OFF = 55000
BACKGROUND_COLOUR = 0x000000
CHECK_DELAY = 1800


class PlantMonitor:
    def __init__(self):
        self.moisture_label = Widgets.Label(
            "11111", 26, 105, 1.0, 0xFFFFFF, BACKGROUND_COLOUR, Widgets.FONTS.DejaVu24
        )
        self.earth_0 = EarthUnit((33, 32))

    def loop(self):
        moisture_value = self.earth_0.get_analog_value()
        self.moisture_label.setText(str(moisture_value))
        if moisture_value > MOISTURE_CUT_OFF:
            self.moisture_label.setColor(0xFF0000, BACKGROUND_COLOUR)
            for count in range(5):
                Speaker.tone(1000, 2000)
                Speaker.stop()
                time.sleep(1)
        else:
            self.moisture_label.setColor(0x3366FF, BACKGROUND_COLOUR)
        time.sleep(CHECK_DELAY)


if __name__ == "__main__":
    try:
        M5.begin()
        time.timezone("GMT+1")
        Speaker.setVolumePercentage(1)
        Widgets.setRotation(0)
        Widgets.fillScreen(BACKGROUND_COLOUR)
        plant_monitor = PlantMonitor()
        while True:
            M5.update()
            plant_monitor.loop()
    except (Exception, KeyboardInterrupt) as e:
        try:
            from utility import print_error_msg

            print_error_msg(e)
        except ImportError:
            print("please update to latest firmware")
