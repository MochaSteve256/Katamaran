#from asyncio.proactor_events import constants
import RPi.GPIO as gp
gp.setwarnings(False)
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

# Create PWM objects
steuerboard_pwm = gp.PWM(st, 100)  # 100 Hz frequency
front_pwm = gp.PWM(fr, 100)         # 100 Hz frequency

# Start PWM
steuerboard_pwm.start(0)  # Start with duty cycle 0 (LED off)
front_pwm.start(0)        # Start with duty cycle 0 (LED off)

# turn off sc
gp.output(sc, True)

def backboard(on: bool):
    if on:
        gp.output(ba, True)
    else:
        gp.output(ba, False)

def steuerboard(on: bool):
    if on:
        # Set duty cycle to 50% (LED fully on)
        steuerboard_pwm.ChangeDutyCycle(30)
    else:
        # Set duty cycle to 0% (LED fully off)
        steuerboard_pwm.ChangeDutyCycle(0)

def front(on: bool):
    if on:
        # Set duty cycle to 50% (LED fully on)
        front_pwm.ChangeDutyCycle(20)
    else:
        # Set duty cycle to 0% (LED fully off)
        front_pwm.ChangeDutyCycle(0)

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
    if not on:
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

# Pre-calculate the maximum wait time (for 4 m out‑and‑back at 343 m/s)
MAX_DISTANCE_CM = 400
SPEED_OF_SOUND_CM_S = 34300
MAX_TIMEOUT = (MAX_DISTANCE_CM * 2) / SPEED_OF_SOUND_CM_S  # ≈0.0233 s

def ultra(timeout=MAX_TIMEOUT):
    # send 10 µs trigger pulse
    gp.output(tr, True)
    time.sleep(0.00001)
    gp.output(tr, False)

    # wait for echo to go high
    start_time = time.time()
    timeout_start = start_time
    while gp.input(ec) == 0:
        start_time = time.time()
        if start_time - timeout_start > timeout:
            # no echo received in time
            return None

    # wait for echo to go low
    stop_time = time.time()
    timeout_start = stop_time
    while gp.input(ec) == 1:
        stop_time = time.time()
        if stop_time - timeout_start > timeout:
            # echo never ended in time
            return None

    # calculate distance
    elapsed = stop_time - start_time
    distance_cm = (elapsed * SPEED_OF_SOUND_CM_S) / 2
    return distance_cm

if __name__ == "__main__":
    while True:
        print(round(ultra(), 2), " cm             ", end="\r")
        time.sleep(0.1)
