from gpiozero import LED
from time import sleep

point = 0.2
tiret = point * 3
espace = point

led = LED(17)

def M(
    led.on()
    sleep(tiret)
    led.off()
    sleep(espace)
    led.on()
    sleep(tiret)
    led.off()
    sleep(espace)
)