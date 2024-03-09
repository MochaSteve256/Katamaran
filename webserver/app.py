from flask import Flask, render_template, Response
from flask_socketio import SocketIO
import cv2

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('joystick_data')
def handle_joystick(data):
    print("Received Joystick Data:", data)

def gen():
    #Video streaming generator function.
    vs = cv2.VideoCapture(0)
    while True:
        ret,frame=vs.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        frame=jpeg.tobytes()
        yield (b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
    vs.release()
    cv2.destroyAllWindows()

@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag.
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/navbar.html')
def navbar():
    return render_template('navbar.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)