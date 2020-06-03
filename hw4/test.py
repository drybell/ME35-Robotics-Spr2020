#!/usr/bin/env pybricks-micropython


# 157.102

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from time import sleep 
import ubinascii, ujson, urequests, utime

import socket 

addr = ("130.64.157.102", 8080)

sock = socket.create_server(addr)


