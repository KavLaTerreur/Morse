from gpiozero import LED
from time import sleep

point = 0.2
tiret = point * 3
espace = point


def E():
    led.on()
    sleep(point)
    led.off()
    sleep(espace)


