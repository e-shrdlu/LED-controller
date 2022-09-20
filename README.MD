# LED-controller
runs a local webserver on a raspberry pi that can control LED lights

## demonstration
[partially complete](https://youtu.be/AsqQsX_ci0I)\
[in development](https://youtu.be/sTNwZXZ2_zA)

## more technical explaination
this code runs a webpage with flask/waitress for controlling neopixel (WS2812) led strips. I recommend running it from a Raspberry Pi connected to an led strip, but if you want you could run it on your own machine for fun without any led's.

For information on how to connect led's to your Raspberry Pi, I used this tutorial https://dordnung.de/raspberrypi-ledstrip/ws2812

## dependencies
required libraries*:
 - flask
 - waitress
 - rpi_ws281x
 
 *you can just run led.py without all the other files if you just want it to run one animation, and in this case you only need the rpi_ws281x library

## warning
much of this code was written in the span of a few weeks, recklessly neglecting the use of comments and irresponibly endangering my future sanity by the absolute refusal to follow any kind of best-practices. As such, if one desires to embark on a simmiliar project of their own, I strongly reccomend that you stray no further down this path. Read this to see the horrors that lie within, then burn it to the ground. With any luck, from the ashes you will be able to piece together your own project
