import pigpio

leftMotor = 4
rightMotor = 17

pi = pigpio.pi()
pi.set_servo_pulsewidth(leftMotor, 1485)
pi.set_servo_pulsewidth(rightMotor, 1485)

maxValue = 2000
minValue = 700

def backbord_speed(speed):
    try:
        speed = int(speed)
    except:
        print("what the hell")
    if speed > maxValue:
        speed = maxValue
    elif speed < minValue:
        speed = minValue
    pi.set_servo_pulsewidth(leftMotor, speed)

def steuerbord_speed(speed):
    try:
        speed = int(speed)
    except:
        print("what the hell")
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
