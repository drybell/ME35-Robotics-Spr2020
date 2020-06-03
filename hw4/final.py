#!/usr/bin/env pybricks-micropython
#brickrun -r -- pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.iodevices import AnalogSensor, UARTDevice

brick.sound.beep()

minimotor = Motor(Port.D)
leftmotor = Motor(Port.C, Direction.CLOCKWISE)
rightmotor= Motor(Port.B, Direction.CLOCKWISE)
robot = DriveBase(leftmotor,rightmotor, 40, 200)
button = TouchSensor(Port.S1)
color = ColorSensor(Port.S2)

#sense = AnalogSensor(Port.S3, False)


direction = 1

while True:
    if button.pressed():
        direction *= -1
    minimotor.run(direction*20)
    robot.drive(direction*0,0)
    data = color.color()
    #uart.write(data)
    wait(500)
    #print(color.color())
