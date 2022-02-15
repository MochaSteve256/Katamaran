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
def moop(running, speed):
    while running:
        gp.output(mo, True)
        time.sleep(1 / 100)
        gp.output(mo, False)
        time.sleep((1 / 100) * speed)
def bastfr(b, s, f):
    if b:
        gp.output(ba, True)
    if not b:
        gp.output(ba, False)
    if s:
        gp.output(st, True)
    if not s:
        gp.output(st, False)
    if f:
        gp.output(fr, True)
    if not f:
        gp.output(fr, False)
def mosc(m, s):
    running = False
    if s:
        gp.output(sc, True)
    if not s:
        gp.output(sc, False)
    if m:
        gp.output(mo, True)
        moop(False, m)
    elif not m:
        gp.output(mo, False)
        moop(False, m)
    if 0 < m < 101:
        moop(True, m)
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