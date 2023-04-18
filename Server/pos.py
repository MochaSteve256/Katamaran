import time
import string
import serial
import pynmea2
import py_qmc5883l
sensor = py_qmc5883l.QMC5883L()
def get_gyro():
    m = sensor.get_magnet_raw()
    return m
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
