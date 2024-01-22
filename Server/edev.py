from asyncio.proactor_events import constants
import RPi.GPIO as gp
import time
import threading
# Pin-Nummern für Geräte einstellen
ba = 33 # Backboard
st = 35 # Steuerboard
fr = 37 # Front
sc = 3 # Scheinwerfer
re = 32 # Ready-LED
co = 36 # Connection-LED
tr = 13 # Trigger (Ultra)
ec = 15 # Echo (Ultra)bastfrreco
sh = 11 # Shutdown-Knopf
ca = 12 # Radar-Kalibrierung
gp.setmode(gp.BOARD)
gp.setup((ba, st, fr, sc, re, co), gp.OUT)
gp.setup((ec, sh), gp.IN)
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
th = threading.Thread(target=conled)
th.start()
def bastfrreco(b, s, f, r, c, sc):
    global constatus
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
    if r == "on":
        gp.output(re, True)
    if r == "off":
        gp.output(re, False)
    if c == "on":
        constatus = 1
    if c == "off":
        constatus = 0
    if sc == "on":
        gp.output(sc, True)
    if sc == "off":
        gp.output(sc, False)

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

if __name__ == "__main__":
    while True:
        sel = input("def: ")
        if sel == "stuff":
            ba = input("backbord_led: ")
            st = input("steuerbord_led: ")
            fr = input("front_led: ")
            re = input("ready_led: ")
            co = input("control_led: ")
            sc = input("flashlight: ")
            bastfrreco(ba, st, fr, re, co, sc)