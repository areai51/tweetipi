# change LED values based on sine cos and tan
from rgbled import rgbled
from random import randint
import time
import math

led = rgbled(22,26,24,50)
gatedoutput =lambda n, minn, maxn: max(min(maxn, n), minn)

try:
    for x in range (360):
        r=math.sin(math.radians(x))*100
        g=math.cos(math.radians(x))*100
        b=math.tan(math.radians(x))*100
        #led.changeto(r,g,b,0.5)
    
        gr=gatedoutput (r, minn, maxn)
        gg=gatedoutput (g, minn, maxn)
        gb=gatedoutput (b, minn, maxn)
        print (gr,gg,gb)
        led.changeto(gr,gg,gb,0.5)
        time.sleep(0.0125)

    led.off(0.8)
    led.cleanup()

except KeyboardInterrupt:
    led.off(0.8)
    led.cleanup()

    
