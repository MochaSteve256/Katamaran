from asyncio.proactor_events import constants
import RPi.GPIO as gp
import time
import threading
# Pin-Nummern für Geräte einstellen
ba = 33 # Backboard
st = 35 # Steuerboard
fr = 37 # Front
sc = 8 # Scheinwerfer
re = 32 # Ready-LED
co = 36 # Connection-LED
tr = 13 # Trigger (Ultra)
ec = 15 # Echo (Ultra)bastfrreco
sh = 11 # Shutdown-Knopf
gp.setmode(gp.BOARD)
gp.setup((ba, st, fr, sc, re, co, tr), gp.OUT) # type: ignore
gp.setup((ec, sh), gp.IN) # type: ignore
running = False
constatus = 0
def conled():
    global constatus
    while 1:
        if constatus == 0:
            gp.output(co, True)
            time.sleep(0.1)
            gp.output(co, False)
            time.sleep(2)
        if constatus == 1:
            gp.output(co, True)
            time.sleep(0.001)
            gp.output(co, False)
            time.sleep(0.002)
con_th = threading.Thread(target=conled)
con_th.start()

steuerboard_led = False
front_led = False

def steuerboardled():
    global backboard_led
    while 1:
        if steuerboard_led:
            gp.output(st, True)
            time.sleep(.01)
            gp.output(st, False)
            time.sleep(.01)
        else:
            gp.output(st, False)

def frontled():
    global backboard_led
    while 1:
        if front_led:
            gp.output(fr, True)
            time.sleep(.01)
            gp.output(fr, False)
            time.sleep(.01)
        else:
            gp.output(fr, False)

st_th = threading.Thread(target=steuerboardled)
fr_th = threading.Thread(target=frontled)
st_th.start()
fr_th.start()

def backboard(on: bool):
    if on:
        gp.output(ba, True)
    else:
        gp.output(ba, False)

def steuerboard(on: bool):
    global steuerboard_led
    steuerboard_led = on

def front(on: bool):
    global front_led
    front_led = on

def ready(on: bool):
    if on:
        gp.output(re, True)
    else:
        gp.output(re, False)

def connection(on: bool):
    global constatus
    if on:
        constatus = 1
    else:
        constatus = 0

def scheinwerfer(on: bool):
    if on:
        gp.output(sc, True)
    else:
        gp.output(sc, False)



def lights(on: bool):
    if on:
        backboard(True)
        steuerboard(True)
        front(True)
    else:
        backboard(False)
        steuerboard(False)
        front(False)

def ultra():
    # set Trigger to HIGH
    gp.output(tr, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    gp.output(tr, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while gp.input(ec) == 0:
        StartTime = time.time()

    # save time of arrival
    while gp.input(ec) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

if __name__ == "__main__":
    while True:
        print(round(ultra(), 2), " cm             ", end="\r")
        time.sleep(0.1)
