#imports
from time import sleep
import RPi.GPIO as GPIO
import sys
#gpio pins of the servos
s1 = 29 #lenk
s2 = 38 #cam x
s3 = 40 #cam y
#GPIO  set up
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(s2, GPIO.OUT)
GPIO.setup(s3, GPIO.OUT)
pwm1=GPIO.PWM(s2, 50)
pwm2=GPIO.PWM(s3, 50)
pwm1.start(0)
pwm2.start(0)
def setcamx(angle):
    angle -= 90
    duty = angle / 18 + 2
    GPIO.output(s2, True)
    pwm1.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(s2, False)
    pwm1.ChangeDutyCycle(0)
def setcamy(angle):
    angle -= 90
    duty = angle / 18 + 2
    GPIO.output(s3, True)
    pwm2.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(s3, False)
    pwm2.ChangeDutyCycle(0)

if __name__ == "__main__":
    #loop
    while True:
        ser = input("x, y?: ")
        x = input(">>> ")#get input
        if x == "exit":
            sys.exit()
        else:
            try:
                x = int(x)#convert input str to int
                if ser == "x":
                    setcamx(x)#set current angle to input value
                elif ser == "y":
                    setcamy(x)#set current angle to input value
            except Exception as e:
                print("Failed with an Exception: ", e)
    #
    # #
    # # # mid value:87-88
    # #
    #
