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
        self._mode('ANALOG')
        return self._value(0)

class EV3Sensor2(Ev3devSensor):
    _ev3dev_driver_name='ev3-analog-0'
    def readvalue(self):
        self._mode('ANALOG')
        return self._value(0)


# this is a hack to set the mode properly
from ev3dev2.port import LegoPort
s = LegoPort(address ='ev3-ports:in1')
s.mode = 'ev3-analog'

s2 = LegoPort(address = 'ev3-ports:in4')
s2.mode = 'ev3-analog'

wait(2000)

# now set up your sensor to read
left=EV3Sensor(Port.S1) # same port as abover
right=EV3Sensor(Port.S4)

right_motor = Motor(Port.D, Direction.CLOCKWISE, [40,12])
left_motor = Motor(Port.A, Direction.CLOCKWISE, [40,12])
# steering = Motor(Port.C)

robot = DriveBase(left_motor, right_motor, 56, 200)

#robot.drive_time(800,0,5000)
#steering.run_time(300, 500)
wait(500)
print(left.readvalue()) 
print(right.readvalue())

# left calibration value: 900
# righty calibration value: 500

# left see black at < 400 
# right see black at < 300


# detected = 0

# robot.drive(100)
# while True:
#     steering.run(150)
#     wait(200)
#     steering.run(-150)


detected = 0

robot.drive(200,0)

while True: 
    print("Left: %(value)s" % {"value": left.readvalue()})
    print("Right: %(value)s" % {"value":right.readvalue()})

    if left.readvalue() <= 800: 
        print("LEFT DETECTED Left: %(value)s" % {"value": left.readvalue()})
        print("LEFT DETECTED Right: %(value)s" % {"value":right.readvalue()})
        robot.drive(100,90)
        robot.stop()
        sleep(20)
        robot.drive_time(-50,0,200)
        
    if right.readvalue() <= 600:
        print("RIGHT DetECTED Left: %(value)s" % {"value": left.readvalue()})
        print("RIGHT DETECTED Right: %(value)s" % {"value":right.readvalue()})
        # turn right
        robot.drive(100,-90)
        robot.stop()
        sleep(20)
        robot.drive_time(-50,0,200)








# detected = 0
# while True:
# 	# print(sensor.readvalue())
#         print("Left: %(value)s" % {"value": left.readvalue()})
#         print("Right: %(value)s" % {"value":right.readvalue()})
#         while(left.readvalue() > 800 and right.readvalue() > 600):
#             detected = 0
#             robot.drive(100, 0)
#             steering.stop()
#             print("Left: %(value)s" % {"value": left.readvalue()})
#             print("Right: %(value)s" % {"value":right.readvalue()})
#         x = 0
#         if(left.readvalue() <= 800):
            # print("LEFT DETECTED Left: %(value)s" % {"value": left.readvalue()})
            # print("LEFT DETECTED Right: %(value)s" % {"value":right.readvalue()})
#             robot.drive(100, 0) 
#             steering.run(-50) 
#             detected = -1
#         if(right.readvalue() <= 600):
            # print("RIGHT DetECTED Left: %(value)s" % {"value": left.readvalue()})
            # print("RIGHT DETECTED Right: %(value)s" % {"value":right.readvalue()})
#             robot.drive(100,0)
#             steering.run(50)
#             detected = 1


