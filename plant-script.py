import os, sys, io
import M5
from M5 import *
import time
from unit import EarthUnit



moisture_label = None
earth_0 = None


moisture_value = None

TOO_DRY_VAL = 55000


def setup():
  global moisture_label, earth_0, moisture_value

  M5.begin()
  Widgets.setRotation(0)
  Widgets.fillScreen(0x000000)
  moisture_label = Widgets.Label("11111", 26, 105, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu24)

  time.timezone('GMT+1')
  earth_0 = EarthUnit((33, 32))
  moisture_value = 0


def loop():
  global moisture_label, earth_0, moisture_value
  M5.update()
  moisture_value = earth_0.get_analog_value()
  moisture_label.setText(str(moisture_value))
  if moisture_value > TOO_DRY_VAL:
    moisture_label.setColor(0xff0000, 0x000000)
  else:
    moisture_label.setColor(0x3366ff, 0x000000)
  time.sleep(5)


if __name__ == '__main__':
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
