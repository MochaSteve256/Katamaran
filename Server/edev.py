import RPi.GPIO as gp
import csocket
import time
import threading
# Pin-Nummern für Geräte einstellen
ba = 33 # Backboard
st = 35 # Steuerboard
fr = 37 # Front
sc = 36 # Scheinwerfer
re = 32 # Ready-LED
mo = 31 # Motor (Antrieb)
tr = 13 # Trigger (Ultra)
ec = 15 # Echo (Ultra)
sh = 11 # Shutdown-Knopf
ca = 12 # Radar-Kalibrierung
gp.setmode(gp.BOARD)
gp.setup((ba, st, fr, sc, re, mo), gp.OUT)
gp.setup((ec, sh), gp.IN)
running = False
speed = 0
def moop():
    global running
    global speed
    while 1:
        while running:
            gp.output(mo, True)
            time.sleep(1 / 100)
            gp.output(mo, False)
            time.sleep((1 / 100) * speed)
t = threading.Thread(target=moop)
t.start()
def bastfr(b, s, f):
    if b == "on":
        gp.output(ba, True)
    if b == "off":
        gp.output(ba, False)
    if s == "on":
        gp.output(st, True)
    if s == "off":
        gp.output(st, False)
    if f == "on":
        gp.output(fr, True)
    if f == "off":
        gp.output(fr, False)
def mosc(m, s):
    if s == "on":
        gp.output(sc, True)
    if s == "off":
        gp.output(sc, False)
    if m == "on":
        gp.output(mo, True)
        running = False
    elif m == "off":
        gp.output(mo, False)
        running = False
    else:
        if 0 < int(m) < 101:
            running = True
            speed = int(m)
def ready(r):
    if r:
        gp.output(re, True)
    if not r:
        gp.output(re, False)
def ultra():
    for i in range(2):
        global a
        global b
        global a1
        global a2
        gp.output(tr, True)
        a = time.time()
        gp.output(tr, False)
        while gp.input(ec) == False and ((b - a) / 2 ) * 343 < 5:
            b = time.time()
        if i == 0:
            a1 = ((b - a) / 2) * 343
        if i == 1:
            a2 = ((b - a) / 2) * 343
    d = (a1 + a2) / 2
    return d
def cal():
    while gp.input(ca) == False:
        time.sleep(0.0001)
    csocket.cal()