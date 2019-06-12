import rain_detector
import dule_color_led
import thermistor

import time

is_raining = False


def init():
    GPIO.setmode(GPIO.BCM)
    rain_detector.setup()
    thermistor.setup()


def is_raining(status):
    return rain_detector.get_status(status)


def get_temperature():
    return thermistor.get_temp()


if __name__ == "main":

    init()

    while True:
        time.sleep(30)
        is_raining = is_raining(is_raining)
        if is_raining:
            dule_color_led.setColor(dule_color_led.colors[0])
            print "raining"
        else:
            dule_color_led.setColor(dule_color_led.colors[1])
            print "not raining"

        print get_temperature()


