import time
from datetime import datetime, timedelta
from threading import Thread
import led_change_handler
import hashlib
import led

"""import os
import argparse

# curl -X POST -F exec="import os;os.system('sudo python3 /home/pi/Desktop/LED_alarm.py 7 30')" 192.168.0.8

keep_awake=False

parser=argparse.ArgumentParser()
parser.add_argument("hour")
parser.add_argument("minute")
args = parser.parse_args()

raspberry_pi_led_controller_ip = "192.168.0.8"

alarm_hour = int(args.hour)
alarm_min = int(args.minute)
"""
current_alarm = [None,None]


def set_alarm(hour,min,pswd):
    global current_alarm
    pswd = hashlib.sha256(pswd.encode()).hexdigest()

    if pswd != led_change_handler.admin_password:
        return -1

    current_alarm = [hour,min]
    now=datetime.now()
    alarm_time = now.replace(hour=hour,minute=min,second=0)

    if now > alarm_time:
        alarm_time += timedelta(days=1)

    """if keep_awake:
        import pyautogui
        def keep_awake_func():
            global keep_awake
            while keep_awake:
                time.sleep(30)
                pyautogui.press("f13")
        keep_awake_thread = Thread(target=keep_awake_func)
        keep_awake_thread.start()"""

    seconds_to_alarm = int((alarm_time - now).total_seconds())
    print("alarm set for",alarm_time,",which is",seconds_to_alarm,"seconds in the future","(or",seconds_to_alarm//3600,"hours)")
    alarm_time = time.time() + seconds_to_alarm
    while time.time() < alarm_time:
        if alarm_time - time.time() < 3600:
            time.sleep(60)
        else:
            time.sleep(3600)
    for clr in range(3):
        led_change_handler.send_choice([(255,0,0),(0,255,0),(0,0,255)][clr], "custom", pswd, custom_func=led.wipe_a)
        led_change_handler.animation_thread.join()
    led_change_handler.send_choice((255,255,255), "custom", pswd, custom_func=led.no_a)
    current_alarm = [None,None]


    # time.sleep(seconds_to_alarm)
    # x = os.system("curl -X POST -F exec=\"led.wipe(strip, led.Color(255,0,0), 0, 1, 1)\" " +raspberry_pi_led_controller_ip+ " && curl -X POST -F choice=no " + raspberry_pi_led_controller_ip)
    # os will print output unless its assigned to variable
    """if keep_awake:
        keep_awake=False
        keep_awake_thread.join()"""
