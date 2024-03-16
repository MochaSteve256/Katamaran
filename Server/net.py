from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
import threading

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


@socketio.on('slider_data')
def handle_slider_data(data):
    global x_value, y_value, timer_x, timer_y
    x = 0 - data.get('x') + 95
    y = data.get('y') + 95

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

def run():
    socketio.run(app, use_reloader=True, log_output=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    run()