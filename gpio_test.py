import RPi.GPIO as gpio
from time import sleep

pin40 = 40

gpio.setmode(gpio.BOARD)

gpio.setup(pin40,gpio.OUT)

for i in range(10):
    gpio.output(pin40,gpio.HIGH)
    sleep(1)
    gpio.output(pin40,gpio.LOW)
    sleep(1)

gpio.cleanup()
