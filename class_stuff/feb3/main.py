#!/usr/bin/env pybricks-micropython
# Daniel Ryaboshapka
# Feb 3 2020


from pybricks import ev3brick as brick
from pybricks.ev3devices import TouchSensor
from pybricks.parameters import (Port, Stop, Button)
from pybricks.tools import wait, StopWatch
from time import *

touch = TouchSensor(Port.S3)

with open("data.txt","a") as f:
    while True:
        now = time()
        if touch.pressed():
            f.write(str(time())+", ")
