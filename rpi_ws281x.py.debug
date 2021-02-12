"""
this script only exists to spoof the rpi_ws281x library for testing purposes on machines not connected to led lights. it will print paramaters given to it instead of actually doing anything.
"""

import time

class Adafruit_NeoPixel():
    def __init__(self, *args, **kwargs):
        print(args,kwargs)
        self.last_printed=time.time()
    def numPixels(self):
        return 300
    def begin(self):
        pass
    def setPixelColor(self,pos,color):
        if 0 or time.time()-self.last_printed > 5:
            print(pos,color)
            self.last_printed=time.time()
    def show(self):
        pass

class Color():
    def __init__(self,r,g,b):
        self.color=(r,g,b)
    def __str__(self):
        return str(self.color)
