from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

import servo

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

x_value = 0
y_value = 0

@socketio.on('slider_data')
def handle_slider_data(data):
    x = 0 - data.get('x') + 95
    y = data.get('y') + 95
    global x_value, y_value
    if x_value is None or y_value is None:
        return
    if x != x_value:
        x_value = x
        servo.setcamx(x_value)
    if y != y_value:
        y_value = y
        servo.setcamy(y_value)

if __name__ == '__main__':
    socketio.run(app, use_reloader=True, log_output=True, host='0.0.0.0', port=5000)
