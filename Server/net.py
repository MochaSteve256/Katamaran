from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

import servo

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('slider_data')
def handle_slider_data(data):
    x_value = data.get('x')
    y_value = data.get('y')
    servo.setcamx(x_value)
    servo.setcamy(y_value)

if __name__ == '__main__':
    socketio.run(app, use_reloader=True, log_output=True, host='0.0.0.0', port=5000)
