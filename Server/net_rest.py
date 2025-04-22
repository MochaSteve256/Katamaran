import subprocess
import os
from flask import Flask, request, jsonify
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
#import pos

running = False

app = Flask(__name__)
CORS(app)

x_value = 0
y_value = 0
timer_x = None
timer_y = None

spotlight_on = False
lMotor_speed = 0
rMotor_speed = 0
lights_on = False

def set_cam_x():
    global x_value, timer_x
    servo.setcamx(x_value)
    timer_x = None

def set_cam_y():
    global y_value, timer_y
    servo.setcamy(y_value)
    timer_y = None

@app.route('/slider', methods=['POST'])
def slider_data():
    global x_value, y_value, timer_x, timer_y
    data = request.json
    x = 0 - data.get('x', 0)
    y = data.get('y', 0)

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

    return jsonify(success=True)

@app.route('/spotlight', methods=['POST'])
def spotlight():
    global spotlight_on
    on = request.json.get('on', False)
    edev.scheinwerfer(on)
    spotlight_on = on
    return jsonify(success=True)

@app.route('/lights', methods=['POST'])
def lights():
    global lights_on
    on = request.json.get('on', False)
    edev.lights(on)
    lights_on = on
    return jsonify(success=True)

@app.route('/motors', methods=['POST'])
def motor_data():
    global lMotor_speed, rMotor_speed
    data = request.json
    lMotor_speed = data.get('b', 0)
    rMotor_speed = data.get('s', 0)
    motors.backbord_speed(lMotor_speed)
    motors.steuerbord_speed(rMotor_speed)
    return jsonify(success=True)

@app.route('/power', methods=['POST'])
def power_mgmt():
    action = request.json.get('action')
    if action == "shutdown":
        os.system("sudo shutdown now")
    elif action == "reboot":
        os.system("sudo reboot")
    return jsonify(success=True)

@app.route('/camera', methods=['POST'])
def camera_mgmt():
    action = request.json.get("action")
    if action == "take":
        # take photo
        pass
    elif action == "start":
        # start recording
        pass
    elif action == "stop":
        # stop recording
        pass
    return jsonify(success=True)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        "slider": {"x": 0 - x_value, "y": y_value},
        "lights": {"on": lights_on},
        "motors": {"b": lMotor_speed, "s": rMotor_speed},
        "spotlight": {"on": spotlight_on}
    })

@app.route('/telemetry', methods=['GET'])
def telemetry():
    dist = edev.ultra()
    if dist is not None:
        dist = edev.ultra()
    else:
        dist = 400
    result = {
        "ultrasonic": round(dist / 100, 2),
        "gyro": {}
    }
    x, y, z = None, None, None
    try:
        x, y, z = pos.get_gyro()
    except:
        print("error getting pos")
    if x is not None and y is not None and z is not None:
        result["gyro"] = {"x": x, "y": y, "z": z}
    return jsonify(result)

def run():
    global running
    running = True
    print("REST API started!")
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    run()
