from gpiozero import Servo
from time import sleep

servo = Servo(17)

def gradualMin():
    for angle in range(10, -11, -1):  
        servo.value = angle / 10
        sleep(0.05)  # Adjust this delay to control the speed of the movement
        
def gradualMax():
    for angle in range(-10, 11, 1):  
        servo.value = angle / 10
        sleep(0.05) 

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
    

#string = "110110011011000011011111011110"
string = "11111100000"

for i in range(0, len(string)):
    if string[i] == "1":
        oneRotation()
    else:
        zeroRotation()
