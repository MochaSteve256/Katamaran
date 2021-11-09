import servo
#loop
while True:
    x = input(">>> ")#get input
    try:
        x = int(x)#convert input str to int
        if 101 > x > -101:
            servo.setrudder(x + 87)#set angle  to input  value
        else:
            print("invalid number")
    except Exception as e:
        print("Failed with an Exception: ", e)
#
# #
# # # mid value:87-88
# #
#