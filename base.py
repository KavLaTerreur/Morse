from gpiozero import led
from time import sleep

point = 0.2
tiret = point * 3
espace = point

led = LED(17)

while True:
    led.on()
    sleep(point)
    led.off()
    sleep(espace)
    led.on()
    sleep(point)
    led.of()
    sleep(espace)


