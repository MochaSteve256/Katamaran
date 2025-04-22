import subprocess
import os
from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
import threading
import time

print("Importing edev.py")
import edev
print("Importing motors.py")
import motors
print("Importing servo.py")
import servo
print("Importing pos.py")
import pos

running = False

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

x_value = 0
y_value = 0
timer_x = None
timer_y = None

def set_cam_x():
    global x_value, timer_x
    servo.setcamx(x_value)
    timer_x = None


def set_cam_y():
    global y_value, timer_y
    servo.setcamy(y_value)
    timer_y = None

def background_thread():
    global running
    while running:
        # emit variable data
        #ultrasonic distance float
        dist = edev.ultra()
        if dist is not None:
            dist = edev.ultra()
        else:
            dist = 400
        socketio.emit('ultrasonic_data', {'distance': round(dist / 100, 2)})
        #gps lat, lng, alt, spd float
        #wifi strength int
        #gyro x, y, z float
        x_v, y_v, z_v  = pos.get_gyro()
        if x_v is not None and y_v is not None and z_v is not None:
            socketio.emit("gyro_data", {"x": x_v, "y": y_v, "z": z_v})
            print("x: " + str(x_v) +  "   y: " + str(y_v) + "   z: " + str(z_v) + "       ")
        time.sleep(.3)

spotlight_on = False
lMotor_speed = 0
rMotor_speed = 0
lights_on = False

@socketio.on('connect')
def handle_connect():
    # emit current states
    #camera x and y int
    global x_value, y_value
    socketio.emit('slider_data', {'x': 0 - x_value, 'y': y_value})
    #lights bool
    global lights_on
    socketio.emit("lights", {"on": lights_on})
    #motor speeds int
    global lMotor_speed, rMotor_speed
    socketio.emit("motor_data", {"b": lMotor_speed, "s": rMotor_speed})
    #spotlight bool
    socketio.emit("spotlight", {"on": spotlight_on})
    global running
    running = True
    socketio.start_background_task(target=background_thread)

@socketio.on("disconnect")
def handle_disconnect():
    global runnning
    running = False

@socketio.on('slider_data')
def handle_slider_data(data):
    global x_value, y_value, timer_x, timer_y
    x = 0 - data.get('x')
    y = data.get('y')

    if timer_x is not None:
        timer_x.cancel()
    if timer_y is not None:
        timer_y.cancel()

    if x_value != x:
        x_value = x
        timer_x = threading.Timer(0.3, set_cam_x)
        timer_x.start()
    if y_value != y:
        y_value = y
        timer_y = threading.Timer(0.3, set_cam_y)
        timer_y.start()

@socketio.on('spotlight')
def handle_spotlight(data):
    edev.scheinwerfer(data.get('on'))
    global spotlight_on
    spotlight_on = data.get("on")

@socketio.on('lights')
def handle_lights(data):
    edev.lights(data.get('on'))
    global lights_on
    lights_on = data.get("on")

@socketio.on('motor_data')
def handle_motor_data(data):
    motors.backbord_speed(data.get('b'))
    motors.steuerbord_speed(data.get('s'))
    global lMotor_speed, rMotor_speed
    lMotor_speed = data.get("b")
    rMotor_speed = data.get("s")

@socketio.on('power_mgmt')
def handle_power_mgmt(data):
    if data.get("action") == "shutdown":
        os.system("sudo shutdown now")
    elif data.get("action") == "reboot":
        os.system("sudo reboot")

@socketio.on("camera_mgmt")
def handle_camera_mgmt(data):
    if data.get("action") == "take":
        #take photo
        pass
    elif data.get("action") == "start":
        #start recording
        pass
    elif data.get("action") == "stop":
        #stop ongoing recording if currently recording
        pass

def run():
    socketio.run(app, use_reloader=False, debug=True, log_output=False, allow_unsafe_werkzeug=True, host='0.0.0.0', port=5000)
    print("Socket started!")
if __name__ == '__main__':
    run()
