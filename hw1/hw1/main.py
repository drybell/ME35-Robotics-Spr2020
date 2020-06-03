#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from time import sleep 

# Motor Definitions 
right_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE, [40,8])
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [40,8])
robot = DriveBase(left_motor, right_motor, 56, 134)
sensor = UltrasonicSensor(Port.S1)
light_sensor = ColorSensor(Port.S4)


# robot.drive(400, 180)
# while True:
#     if light_sensor.reflection() < 10:
#         robot.stop(Stop.BRAKE)
#         robot.drive_time(-400, 0, 1250)
#         robot.drive_time(-400, 180, 1000)
#     while sensor.distance() < 2500:
#         if light_sensor.reflection() < 10:
#             robot.stop(Stop.BRAKE)
#             robot.drive_time(-300, 180, 1000)
#         if sensor.distance() < 100: 
#             robot.drive(-100,0)
#         elif sensor.distance() >= 1000:
#             robot.drive(100, 180)
#         elif sensor.distance() < 1000:
#             robot.drive_time(3000, 0,4000)
#             if light_sensor.reflection() < 10:
#                 robot.stop(Stop.BRAKE)
#                 robot.drive_time(-300, 180, 1000)
#             robot.drive(-500, 180)
#         else:
#             robot.drive_time(400,120, 500)
        

# robot.stop()

# wait(3000)
# robot.drive_time(4000, -20, 5000)