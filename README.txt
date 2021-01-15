this code runs a webpage with flask/waitress for controlling neopixel (WS2812) led strips. I recommend running it from a Raspberry Pi connected to an led strip, but if you want you could run it on your own machine for fun without any led's.
For information on how to connect led's to your Raspberry Pi, I recommend this tutorial https://dordnung.de/raspberrypi-ledstrip/ws2812

required libraries*:
flask, waitress, rpi_ws281x
*you can just run led.py without all the other files if you just want it to run one animation, and in this case you only need the rpi_ws281x library

a lot of this was written by copying some example code and modifying/expanding on it, and as such there may be things that there doesn't appear to be any reason for because they got copied over and I didn't understand them so I left them in.

what am I supposed to put in a readme
