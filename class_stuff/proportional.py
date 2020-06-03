#!/usr/bin/env pybricks-micropython

# Daniel Ryaboshapka
# Jan 27 2020


from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from time import sleep

left = Motor(Port.A)
right = Motor(Port.C)
dist = UltrasonicSensor(Port.S4)
wheel_dia = 56
wheel_spacing = 200

car = DriveBase(left,right,wheel_dia,wheel_spacing)

#ms = kp(pd - p)

# threshold distance = 10cm 
while True:
	with open("data.txt", "a") as f:
		distance = dist.distance()
		#proportional speed 
		ratio = (distance / 100)

		speed = ratio * (distance - 100)
		correct_string = str(distance) + ", "
		f.write(correct_string)

		car.drive(speed, 0)
