import pigpio

leftMotor = 17
rightMotor = 4

pi = pigpio.pi()
pi.set_servo_pulsewidth(leftMotor, 1485)
pi.set_servo_pulsewidth(rightMotor, 1485)

offset = 1485
maxValue = 2000
minValue = 700

def backbord_speed(speed: int):
    speed = -speed
    speed += offset
    if speed > maxValue:
        speed = maxValue
    elif speed < minValue:
        speed = minValue
    pi.set_servo_pulsewidth(leftMotor, speed)

def steuerbord_speed(speed: int):
    speed += offset
    if speed > maxValue:
        speed = maxValue
    elif speed < minValue:
        speed = minValue
    pi.set_servo_pulsewidth(rightMotor, speed)

if __name__ == "__main__":
    while True:
        b = input("backbord_speed: ")
        try:
            b = int(b)
        except:
            print("what the hell")
            b = 0
        backbord_speed(b)
        s = input("steuerbord_speed: ")
        try:
            s = int(s)
        except:
            print("what the hell")
            s = 0
        steuerbord_speed(s)
