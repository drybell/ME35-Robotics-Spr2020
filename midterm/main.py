#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                         InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                         SoundFile, ImageFile, Align)
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from time import sleep 
import ubinascii, ujson, urequests, utime


right_motor = Motor(Port.D, Direction.CLOCKWISE, [40,8,40,8])
left_motor = Motor(Port.A, Direction.CLOCKWISE, [40,8,40,8])
#robot = DriveBase(left_motor, right_motor, 56, 134)
upper_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
timmy_turner = Motor(Port.B, Direction.CLOCKWISE)

us = UltrasonicSensor(Port.S1)
test_button = TouchSensor(Port.S2)

### 
#      TEST RUN: Gather test data by bumping the speed up 
#                by 100 every 3 trials and gather distance
#                Run AI and calculate physics post data-gathering
### 


### Every time the button is pressed, tick up to 3 from 0
### once 3, reset and increase speed by 100 
###  Print Current speed tested, document distance


### Test Medium Motor for optimal movement so ball consistently shoots


distance_record = []

def moveBall():
    timmy_turner.run_angle(300,360)
    wait(100)

#right_motor.run(200)
#left_motor.run(200)
#wait(100)
#right_motor.run(800)
#left_motor.run(800)
#wait(50)
#right_motor.run(2000)
#left_motor.run(2000)
#timmy_turner.run_angle(500,180)
#while True:
    #print(us.distance())
    #upper_motor.run(8000)
    #right_motor.run(8000)
    #left_motor.run(8000)
#wait(500)
#robot.stop()


#always run upper motor at max speed
#vary bottom motor speed for distance change
#ramp up speed for 
def startMotors(speed):
    upper_motor.run(8000)
    for i in [3,2,1]:
        right_motor.run(speed/i)
        left_motor.run(speed/i)
        wait(100)
    right_motor.run(speed)
    left_motor.run(speed)
    wait(2000)


def runTest(speed, count):
    global distance_record
    if (count == 3):
        count = 0
        speed += 150 

    startMotors(speed)
    moveBall()
    print("Speed was: %d" %(speed))
    distance = input("Input (Distance, Success): ")
    distance_record.append(distance)
    count += 1
    return (speed, count)

def main():
    speed = 3100
    count = 0 
    for i in range(30):
        while test_button.pressed() == False:
            print("waiting")
            wait(250)
        (speed, count) = runTest(speed, count)
        print(str(speed) + "  " + str(count))
    with open("distance.txt","w") as f:
        for item in distance_record:
            f.write(distance_record)

if __name__ == '__main__':
    main()
