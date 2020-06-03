#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.iodevice import UART Device
 brick.sound.beep()

 minimotor = Motor(Port.D)
 button = TouchSensor(Port.S1)
 direction = 1

 while True:
     if button.pressed():
         direction *= -1
         print('pressed')
     minimotor.run(direction*10)
