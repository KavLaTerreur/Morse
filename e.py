from gpiozero import LED
from time import sleep




def E():
    point = 0.2
    tiret = point * 3
    espace = point

    led = LED(17)
    led.on()
    sleep(point)
    led.off()
    sleep(espace)


