# randomly change LED values
from rgbled import rgbled
from random import randint
import time
import math

led = rgbled(22,26,24,100)

try:
    t_end =time.time()+5
    while time.time()<t_end:
    # while True:
        r = randint(0,100)
        g = randint(0,100)
        b = randint(0,100)
        led.changeto(r,g,b,0.5)
        time.sleep(0.25)
    led.off(0.8)
    led.cleanup()    
    

except KeyboardInterrupt:
    led.off(0.8)
    led.cleanup()

    
