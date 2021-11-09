#!/usr/bin/python3
import os
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
steer_option = 0
prompt = 0
os.system('clear')
print("Starting...")
GPIO.output(33, GPIO.HIGH)
GPIO.output(35, GPIO.HIGH)
GPIO.output(37, GPIO.HIGH)
sleep(0.5)
GPIO.output(37, GPIO.LOW)
pwm=GPIO.PWM(29, 50)
pwm.start(0)
def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(29, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(29, False)
    pwm.ChangeDutyCycle(0)
SetAngle(0)
sleep(0.2)
SetAngle(180)
sleep(0.2)
SetAngle(90)
GPIO.output(31, GPIO.HIGH)
sleep(0.2)
GPIO.output(31, GPIO.LOW)
print("Ready!")
def co_opt():
    steer_option = input(">>>>> ")
    if steer_option == 'A':
        GPIO.output(33, GPIO.LOW)
        SetAngle(0)
        GPIO.output(33, GPIO.HIGH)
    if steer_option == 'a':
        GPIO.output(33, GPIO.LOW)
        SetAngle(30)
        GPIO.output(33, GPIO.HIGH)
    if steer_option == 's':
        GPIO.output(31, GPIO.LOW)
        GPIO.output(33, GPIO.LOW)
        GPIO.output(35, GPIO.LOW)
        SetAngle(90)
        GPIO.output(33, GPIO.HIGH)
        GPIO.output(35, GPIO.HIGH)
    if steer_option == 'd':
        GPIO.output(35, GPIO.LOW)
        SetAngle(135)
        GPIO.output(35, GPIO.HIGH)
    if steer_option == 'D':
        GPIO.output(35, GPIO.LOW)
        SetAngle(180)
        GPIO.output(35, GPIO.HIGH)
    if steer_option == 'W':
        GPIO.output(31, GPIO.LOW)
    if steer_option == 'w':
        GPIO.output(31, GPIO.HIGH)
    if steer_option == 'h':
        Help()
    if steer_option == 'help':
        Help()
    if steer_option == 'p':
        prompt = input("LXTerminal>>> ")
        os.system(prompt)
    if steer_option == '2':
       GPIO.output(37, GPIO.LOW)
    if steer_option == '1':
        GPIO.output(37, GPIO.HIGH)
def Help():
    print("Cockpit options:")
    print("A: LEFT      a: left       s: middle   d: right     D: RIGHT")
    print("w: Motor ON  W: Motor OFF  1: Lamp ON  2: Lamp OFF")
    print("p: system prompt (cd doesn't work.)")
    print("h / help: This help")
try:
    while True:
        co_opt()
except KeyboardInterrupt:
    print("\n")
    print("Thanks for using this program.")
    sleep(0.5)
    print("Exiting...")
    SetAngle(90)
    pwm.stop()
    GPIO.output(29, GPIO.LOW)
    GPIO.output(31, GPIO.LOW)
    GPIO.output(33, GPIO.LOW)
    GPIO.output(35, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)
    GPIO.cleanup()
    os.system('clear')