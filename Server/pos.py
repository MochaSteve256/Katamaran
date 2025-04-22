import time
import string
import serial
import pynmea2
import py_qmc5883l
import math
print("Initializing QMC")
sensor = py_qmc5883l.QMC5883L()
print("QMC initialized")
time.sleep(1)
def get_gyro():
    x_raw, y_raw, z_raw = sensor.get_magnet_raw()
    if x_raw is None or y_raw is None or z_raw is None:
        return None, None, None

    # Calculate angles for each axis in degrees
    x_angle = math.atan2(y_raw, z_raw) * 180 / math.pi
    y_angle = math.atan2(z_raw, x_raw) * 180 / math.pi
    z_angle = math.atan2(x_raw, y_raw) * 180 / math.pi

    return x_angle, y_angle, z_angle
def get_loc():
    global gps
    port = "/dev/ttyAMA0"
    ser = serial.Serial(port, baudrate=9600, timeout=0.5)
    dataout = pynmea2.NMEAStreamReader()
    newdata = ser.readline()
    if newdata[0:6] == "$GPRMC":
        newmsg = pynmea2.parse(newdata)
        lat = newmsg.latitude
        lng = newmsg.longitude
        alt = newmsg.altidude
        spd = newmsg.spd_over_grnd
        gps = [str(lat), str(lng), str(alt), str(spd)]
        return gps

if __name__ == '__main__':
    while True:
        x_degrees, y_degrees, z_degrees = get_gyro()
        print("X-axis: {:.2f}   ".format(x_degrees), end="")
        print("Y-axis: {:.2f}   ".format(y_degrees), end="")
        print("Z-axis: {:.2f}   ".format(z_degrees), end="\r")
        time.sleep(0.5)
