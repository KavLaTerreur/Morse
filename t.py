
from gpiozero import LED
from time import sleep



def T():
    point = 0.2
    tiret = point * 3
    espace = point

    led = LED(17)
    led.on()
    sleep(tiret)
    led.off()

