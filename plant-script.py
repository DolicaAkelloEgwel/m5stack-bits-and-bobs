import os, sys, io
import M5
from M5 import *
import time
from unit import EarthUnit

moisture_label = None
earth_0 = None
moisture_value = 0
MOISTURE_CUT_OFF = 55000
BACKGROUND_COLOUR = 0x000000
CHECK_DELAY = 1800


def setup():
    global moisture_label, earth_0
    M5.begin()
    Widgets.setRotation(0)
    Widgets.fillScreen(BACKGROUND_COLOUR)
    moisture_label = Widgets.Label(
        "11111", 26, 105, 1.0, 0xFFFFFF, BACKGROUND_COLOUR, Widgets.FONTS.DejaVu24
    )
    time.timezone("GMT+1")
    earth_0 = EarthUnit((33, 32))
    Speaker.setVolumePercentage(1)


def loop():
    global moisture_label, earth_0
    M5.update()
    moisture_value = earth_0.get_analog_value()
    moisture_label.setText(str(moisture_value))
    if moisture_value > MOISTURE_CUT_OFF:
        moisture_label.setColor(0xFF0000, BACKGROUND_COLOUR)
        for count in range(5):
            Speaker.tone(1000, 2000)
            Speaker.stop()
            time.sleep(1)
    else:
        moisture_label.setColor(0x3366FF, BACKGROUND_COLOUR)
    time.sleep(CHECK_DELAY)


if __name__ == "__main__":
    try:
        setup()
        while True:
            loop()
    except (Exception, KeyboardInterrupt) as e:
        try:
            from utility import print_error_msg

            print_error_msg(e)
        except ImportError:
            print("please update to latest firmware")
