import pigpio

leftMotor = 4
rightMotor = 14

pi = pigpio.pi()
pi.set_servo_pulsewidth(leftMotor, 0)
pi.set_servo_pulsewidth(rightMotor, 0)

maxValue = 2000
minValue = 700

def backbord_speed(speed):
    if speed > maxValue:
        speed = maxValue
    elif speed < minValue:
        speed = minValue
    pi.set_servo_pulsewidth(leftMotor, speed)

def steuerbord_speed(speed):
    if speed > maxValue:
        speed = maxValue
    elif speed < minValue:
        speed = minValue
    pi.set_servo_pulsewidth(rightMotor, speed)

if __name__ == "__main__":
    while True:
        b = input("backbord_speed: ")
        backbord_speed(b)
        s = input("steuerbord_speed: ")
        steuerbord_speed(s)