from gpiozero import LED
from time import sleep



def A():
    point = 0.2
    tiret = point * 3
    espace = point

    led = LED(17)
    led.on()
    sleep(point)
    led.off()
    sleep(espace)
    led.on()
    sleep(tiret)
    led.off()
    sleep(espace)

