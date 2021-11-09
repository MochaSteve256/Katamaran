#imports
from time import sleep
import RPi.GPIO as GPIO
#gpio pins of the servos
s1 = 29 #lenk
s2 = 38 #cam x
s3 = 40 #cam x
#GPIO  set up
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(s1, GPIO.OUT)
GPIO.setup(s2, GPIO.OUT)
GPIO.setup(s3, GPIO.OUT)
pwm=GPIO.PWM(s1, 50)
pwm1=GPIO.PWM(s2, 50)
pwm2=GPIO.PWM(s3, 50)
pwm.start(0)
pwm1.start(0)
pwm2.start(0)
def setrudder(angle):
    duty = angle / 18 + 2
    GPIO.output(s1, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(s1, False)
    pwm.ChangeDutyCycle(0)
def setcamx(angle):
    duty = angle / 18 + 2
    GPIO.output(s2, True)
    pwm1.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(s2, False)
    pwm1.ChangeDutyCycle(0)
def setcamy(angle):
    duty = angle / 18 + 2
    GPIO.output(s3, True)
    pwm2.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(s3, False)
    pwm2.ChangeDutyCycle(0)