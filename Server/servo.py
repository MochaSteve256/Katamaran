from time import sleep
import RPi.GPIO as GPIO
s1 = 29
s2 = 
s3 = 
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