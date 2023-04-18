# LED-controller
Flask webpage on Raspberry Pi controls neopixel LED lights to display custom patterns and animations

## demonstration

### Partially Complete

https://user-images.githubusercontent.com/50746727/232639897-3db1237c-4763-4577-adc2-e67364af80c7.mp4


### In Development



https://user-images.githubusercontent.com/50746727/232640868-0c700c0a-fdbd-4289-a343-6a75d977c595.mp4




## more technical explaination
this code runs a webpage with flask/waitress for controlling neopixel (WS2812) led strips plugged into a Raspberry Pi Zero

See this [tutorial](https://dordnung.de/raspberrypi-ledstrip/ws2812) for instructions on connected LEDs to a Raspberry Pi

## dependencies
required libraries:
 - flask*
 - waitress*
 - rpi_ws281x
 
 *required to run web server, lights can be controlled directly from the Raspberry Pi without these

## warning
much of this code was written in the span of a few weeks, recklessly neglecting the use of comments and irresponibly endangering my future sanity by the absolute refusal to follow any kind of best-practices. As such, if one desires to embark on a simmiliar project of their own, I strongly reccomend that you stray no further down this path. Read this to see the horrors that lie within, then burn it to the ground. With any luck, from the ashes you will be able to piece together your own project
