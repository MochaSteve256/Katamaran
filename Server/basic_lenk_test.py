#imports
from time import sleep
import RPi.GPIO as GPIO
#GPIO  set up
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.OUT)
pwm=GPIO.PWM(29, 50)
pwm.start(0)
#definition
def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(29, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(29, False)
    pwm.ChangeDutyCycle(0)
#input loop
while True:
    x = input(">>> ")#get input
    try:
        x = int(x)#convert input str to int
        if 101 > x > -101:
            SetAngle(x + 87)#set angle  to input  value
        else:
            print("invalid number")
    except Exception as e:
        print("Failed with an Exception: ", e)
#
# #
# # # mid value:87-88
# #
#