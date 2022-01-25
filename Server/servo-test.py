import sys
import servo
#loop
while True:
    ser = input("r, x, y?: ")
    x = input(">>> ")#get input
    if x == "exit":
        sys.exit()
    else:
        try:
            x = int(x)#convert input str to int
            if ser == "r":
                servo.setrudder(x + 87)#add input value to current angle
            elif ser == "x":
                servo.setcamx(x)#set current angle to input value
            elif ser == "y":
                servo.setcamy(x)#set current angle to input value
        except Exception as e:
            print("Failed with an Exception: ", e)
#
# #
# # # mid value:87-88
# #
#
