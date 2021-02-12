import hashlib
import time
from datetime import datetime, timedelta
from threading import Thread
import led_change_handler
import led

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
    led_change_handler.send_choice((255,255,255), "custom", pswd, custom_func=led.fast_flowing_rainbow_a)
    current_alarm = [None,None]
