"""from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET'])
def dropdown():
    colours = ['Red', 'Blue', 'Black', 'Orange']
    return render_template('test.html', colours=colours)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=80)

@app.route("/sign-up")
def sign_up():
    return render_template("public/sign_up.html")


"""
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

try:
    with open("/home/pi/Desktop/webserver/pswd.txt",'r') as f:
        admin_password=f.readline().replace("\n","")
except:
    admin_password="change this code later"
need_pswd = False
strip = led.setup()
choices = led.animations

def toggle_pswd(submitted_password):
    global need_pswd, admin_password
    if submitted_password == admin_password:
        need_pswd = not need_pswd

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def main():
    global choices, need_pswd, strip
    if request.method == "POST":
        req = dict(request.form)
        """while 0:
            inp=input(">>")
            try:
                exec(inp)
            except:
                pass
            finally:
                if inp == "quit()":
                    break"""
        if "password" in req.keys():
            req["password"] = hashlib.sha256(req.get("password").encode()).hexdigest()
        if "choice" in req.keys():
            send_choice(req)
            """
            if "password" in dict(req).keys():
                password = req["password"]
                #send_choice(r,g,b,choice,password)
            elif not need_pswd:
                pass
                #send_choice(r,g,b,choice,"none")"""
        elif "password" in req.keys():
            password = req["password"]
            toggle_pswd(password)
        elif "exec" in req.keys():
            code=req.get("exec")
            try:
                exec(code)
            except:
                pass
            finally:
                if code == "exit":
                    quit()

    return render_template('index.html',choices=list(choices.keys()),password_needed=need_pswd)

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

def send_choice(req): # r,g,b,choice,submitted_password):
    global strip, current_animation, current_animation_function, current_animation_thread, need_pswd, admin_password

    if req.get("password",0) == admin_password or not need_pswd:
        r,g,b = [get_int(req.get(x,0)) for x in ["red","green","blue"]]
        rainbow_val = get_int(req.get("rainbow_val",0),max=765)

        """if rainbow_val >= 765:
            rainbow_val=765
        elif rainbow_val <= 0:
            rainbow_val = 0"""

        if rainbow_val:
            r,g,b = led.rainbowWheel(rainbow_val, False)

        choice = req.get("choice", "set color")

        led.go = False
        current_animation_thread.join()
        led.go = True
        current_animation = choices[choice] if choice in choices.keys() else choices["set color"]
        def current_animation_function():
            current_animation(strip,(r,g,b))
        current_animation_thread = Thread(target=current_animation_function)
        current_animation_thread.start()


def dummy_animation():
    pass

if __name__=="__main__":
    current_animation_function=dummy_animation
    current_animation_thread = Thread(target=current_animation_function)
    current_animation_thread.start()
    serve(app,host='0.0.0.0',port=80,url_scheme="https")
    # app.run(debug=True,host='0.0.0.0',port=80)
