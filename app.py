# scp *.py pi@192.168.0.8:/home/pi/Desktop/webserver

# ipconfig && D: && cd D:\Coding\allpython\0raspiLED\flask && py -m http.server
# ssh pi@192.168.0.8 "curl 192.168.0.198:8000/app.py > ~/Desktop/webserver/app.py && curl 192.168.0.198:8000/templates/index.html > ~/Desktop/webserver/templates/index.html && curl 192.168.0.198:8000/led.py > ~/Desktop/webserver/led.py && curl 192.168.0.198:8000/pswd.txt > ~/Desktop/webserver/pswd.txt && sudo python3 ~/Desktop/webserver/app.py"
# ssh pi@192.168.0.8 "curl 192.168.0.198:8000/led.py > ~/Desktop/webserver/led.py && sudo reboot python3 ~/Desktop/webserver/app.py"

# curl -X POST -F red=12 -F green=33 -F blue=2 -F rainbow_val= -F choice="set color" http://192.168.0.8

from flask import Flask, render_template, request, redirect
from waitress import serve
import led
from threading import Thread
import hashlib
import alarm_handler
import led_change_handler


app = Flask(__name__)
debug=1 # 0=no debugging, 1=minimal, 2=max


@app.route("/", methods=["GET","POST"])
def main():
    global need_pswd, strip
    if request.method == "POST":
        req = dict(request.form)
        led_change_handler.main(req)
    return render_template('index.html',choices=list(led.animations.keys()),password_needed=led_change_handler.need_pswd)


@app.route("/alarm", methods=["GET", "POST"])
def alarm():
    if request.method == "POST":
        req = dict(request.form)
        if "hour" in req.keys() and "minute" in req.keys():
            hour = led_change_handler.get_int(req["hour"], max=24)
            min = led_change_handler.get_int(req["minute"],max=60)
            pswd = req["password"]
            alarm_thread = Thread(target=alarm_handler.set_alarm, args=(hour,min,pswd))
            alarm_thread.start()
    return render_template('alarm.html', next_alarm=alarm_handler.current_alarm)


if __name__=="__main__":
    if debug < 2:
        serve(app,host='0.0.0.0',port=80,url_scheme="https")
    if debug >= 2:
        app.run(debug=True,host='0.0.0.0',port=80)
