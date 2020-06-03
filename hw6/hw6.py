#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
brick.sound.beep()
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.iodevices import AnalogSensor, UARTDevice
import time
import random

# Write your program here
ev3 = EV3Brick()
ev3.speaker.beep()

#define sensors and motors
belt = Motor(Port.A)
gate = Motor(Port.C)
uart= UARTDevice(Port.S1,9600, timeout=2000)
light = ColorSensor(Port.S2)

gate.reset_angle(0)
def handshake():
    while uart.waiting()== 0:
        print('Dan\'s nuts')
        wait(10)
    print(uart.read(uart.waiting()))
def reader(): # This function waits for a signal from the uart port, and returns a boolean depending on what the signal is
    while uart.waiting() == 0:
        wait(10)
    signal = uart.read()
    if signal == b'1':
        return True
    else:
        return False
def open_gate(): #opens gate
    gate.run_target(300,-155,Stop.BRAKE,True)
def close_gate(): #closes gate
    gate.run_target(300,0,Stop.BRAKE,True)
def check_brick(): #observe whether there is a brick
    ref = light.reflection()
    if ref > 1:
        return True
    else:
        return False
def is_red():
    belt.run(0)
    uart.write('1')
    response = reader()
    return response

handshake()
while True: # this loop runs the conveyor belt and senses for an object
    belt.run(150)
    is_brick = check_brick()
    print(is_brick)
    if is_brick == True:
        response = is_red()
        if response == True:
            close_gate()
        else:
            open_gate()
        belt.run(150)
        wait(500)