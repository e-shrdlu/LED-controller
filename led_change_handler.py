import led
import app
import hashlib
from threading import Thread


with open("/home/pi/Desktop/webserver/pswd.txt",'r') as f: # pswd.txt should contain sha256 hash of your chosen admin password
    admin_password=f.readline().replace("\n","")

def dummy_animation():
    pass
animation_thread=Thread(target=dummy_animation)
animation_thread.start()

need_pswd = False
strip = led.setup()
choices = led.animations
default_choice = "set color"


def toggle_pswd(submitted_password):
    global need_pswd, admin_password
    if submitted_password == admin_password:
        need_pswd = not need_pswd


def get_int(num, max=255,min=0):
    try:
        num = int(num)
    except:
        num = min
    finally:
        if num <= max:
            return num
        else:
            return max


def send_choice(rgb, choice, submitted_password, custom_func=None, custom_thread=None):
    global strip, animation_thread, need_pswd, admin_password

    if submitted_password == admin_password or not need_pswd:
        led.go = False
        animation_thread.join()
        led.go = True

        if choice == "custom" and custom_func:
            animation_thread = Thread(target=custom_func,args=(strip,rgb))
        elif choice == "custom" and custom_thread:
            animation_thread = custom_thread
        else:
            animation_thread = Thread(target=choices[choice], args=(strip,rgb))
        animation_thread.start()


def main(req):
    global default_choice

    if "delay" in req.keys():
        time.sleep(int(req["delay"]))

    if "password" in req.keys():
        req["password"] = hashlib.sha256(req.get("password").encode()).hexdigest()

    if "choice" in req.keys():
        if req.get("rainbow_val",0):
            r,g,b = led.rainbowWheel(get_int(req["rainbow_val"],max=765), False)
        else:
            r,g,b = [get_int(req.get(x,0)) for x in ["red","green","blue"]]
        send_choice((r,g,b),req.get("choice", default_choice), req.get("password", 0))
    elif "password" in req.keys():
        toggle_pswd(req["password"])
    elif app.debug >= 1 and "exec" in req.keys():
        code=req.get("exec")
        try:
            exec(code)
        except:
            pass
