from gpiozero import Servo
from time import sleep

# select the GPIO pin for control
servo = Servo(17)

# the next two functions were considered to lengthen the amount of time it takes for the servo to turn. The issues we were facing were largely resolved when we
# increased the framerate of the radar.
def gradualMin():
    for angle in range(10, -11, -1):  
        servo.value = angle / 10
        sleep(0.05)  # Adjust this delay to control the speed of the movement
        
def gradualMax():
    for angle in range(-10, 11, 1):  
        servo.value = angle / 10
        sleep(0.05) 

# The next two functions are used to rotate the reflector to indicate either a binary 1 or 0
def oneRotation():
    sleep(0.2)
    servo.min()
    sleep(0.4)
    servo.max()


def zeroRotation():
    sleep(0.2)
    servo.min()
    sleep(1.0)
    servo.max()
    

# modify this string to whatever binary string you would like to send
string = "11111100000"

# loop through all the bits, rotating the corner reflector accordingly
for i in range(0, len(string)):
    if string[i] == "1":
        oneRotation()
    else:
        zeroRotation()
