from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
import threading

import edev
import motors
import servo

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

@socketio.on('connect')
def handle_connect():
    # emit current states
    #camera x and y int
    global x_value, y_value
    socketio.emit('slider_data', {'x': 0 - x_value - 90, 'y': y_value - 90})
    #spotlight bool
    #motor speeds int

    # emit variable data
    #ultrasonic distance float
    #gps lat, lng, alt, spd float
    #wifi strength int
    #gyro x, y, z float

@socketio.on('slider_data')
def handle_slider_data(data):
    global x_value, y_value, timer_x, timer_y
    x = 0 - data.get('x') + 90
    y = data.get('y') + 90

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

@socketio.on('lights')
def handle_lights(data):
    edev.lights(data.get('on'))

@socketio.on('motor_data')
def handle_motor_data(data):
    motors.backbord_speed(data.get('b'))
    motors.steuerbord_speed(data.get('s'))

def run():
    socketio.run(app, use_reloader=False, debug=True, log_output=False, allow_unsafe_werkzeug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    run()
