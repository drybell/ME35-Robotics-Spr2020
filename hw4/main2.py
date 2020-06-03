#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devio import Ev3devSensor


class EV3Sensor(Ev3devSensor):
    _ev3dev_driver_name='ev3-analog-01'
    def readvalue(self):
        self._mode('ev3-uart')
        return self._value(0)

class EV3Sensor2(Ev3devSensor):
    _ev3dev_driver_name='ev3-analog-0'
    def readvalue(self):
        self._mode('ANALOG')
        return self._value(0)


# this is a hack to set the mode properly
from ev3dev.port import LegoPort
s = LegoPort(address ='ev3-ports:in1')
s.mode = 'ev3-uart'

wait(2000)

# now set up your sensor to read
left=EV3Sensor(Port.S1) # same port as abover