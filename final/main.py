#!/usr/bin/env pybricks-micropython

# G3tH4CK3DM4T3

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
import time 
import ubinascii, ujson, urequests, utime

# StartMotors then moveball to set it moving 


starter = Motor(Port.A, Direction.COUNTERCLOCKWISE)
stage_1 = Motor(Port.B, Direction.CLOCKWISE)
stage_2 = Motor(Port.D, Direction.CLOCKWISE)
stage_3 = Motor(Port.C, Direction.COUNTERCLOCKWISE)
# touch = TouchSensor(Port.S1)
# left_motor = Motor(Port.A, Direction.CLOCKWISE, [40,8,40,8])
# #robot = DriveBase(left_motor, right_motor, 56, 134)
# upper_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
# timmy_turner = Motor(Port.B, Direction.CLOCKWISE)

tag = "Start28"

def Get_SL(Tag):
    Key = "bvd8X9LweQY9o2eP1NYL-p8mLL9wMAk6YYOnYSiIo0"
    urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
    headers = {"Accept":"application/json","x-ni-api-key":Key}
    urlValue = urlBase + Tag + "/values/current"
    try:
        value = urequests.get(urlValue,headers=headers).text
        data = ujson.loads(value)
        #print(data)
        result = data.get("value").get("value")
    except Exception as e:
        print(e)
        result = 'failed'
    return result

def Put_SL(Tag, Type, Value):

    Key = "bvd8X9LweQY9o2eP1NYL-p8mLL9wMAk6YYOnYSiIo0"
    urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
    headers = {"Accept":"application/json","x-ni-api-key":Key}
    urlValue = urlBase + Tag + "/values/current"
    propValue = {"value":{"type":Type,"value":Value}}
    try:
        reply = urequests.put(urlValue,headers=headers,json=propValue).text
    except Exception as e:
        print(e)         
        reply = 'failed'
    return reply



def Get_SL_Tensor(Tag):
    TENSORKEY = "j2m40Z2Dd2MyPJcsmCSh586VCtvx68ltYwJjZCHujB"
    urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
    headers = {"Accept":"application/json","x-ni-api-key":TENSORKEY}
    urlValue = urlBase + Tag + "/values/current"
    try:
        value = urequests.get(urlValue,headers=headers).text
        data = ujson.loads(value)
        #print(data)
        result = data.get("value").get("value")
    except Exception as e:
        print(e)
        result = 'failed'
    return result

def Put_SL_Tensor(Tag, Type, Value):
    TENSORKEY = "j2m40Z2Dd2MyPJcsmCSh586VCtvx68ltYwJjZCHujB"
    urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
    headers = {"Accept":"application/json","x-ni-api-key":TENSORKEY}
    urlValue = urlBase + Tag + "/values/current"
    propValue = {"value":{"type":Type,"value":Value}}
    try:
        reply = urequests.put(urlValue,headers=headers,json=propValue).text
    except Exception as e:
        print(e)         
        reply = 'failed'
    return reply
# def setSpeed(cupDistance):
#     #optimalmotorspeed = 347.76(cupdistance) + 597.87
#     speed = int(347.76 * cupDistance + 600)
#     reply = Put_SL("Speed Output", "STRING", str(speed))
#     return speed

# def cupDistance(ultradistance):
#     #cup_distance = .0069(ultrasonic_distance) + .8866 
#     cup_distance = .0069 * ultradistance + .8866
#     return round(cup_distance*2)/2

# def averageUltra():
#     totals = 0
#     for i in range(5):
#         totals += us.distance()
#         time.sleep(.2)
#     distance = totals/5
#     reply = Put_SL("Distance Output", "STRING", str(distance))
#     return distance

# def moveBall():
#     timmy_turner.run_angle(500,360)

#always run upper motor at max speed
#vary bottom motor speed for distance change
#ramp up speed for 
# def startMotors(speed):
#     upper_motor.run(8000)
#     for i in [3,2,1]:
#         right_motor.run(speed/i)
#         left_motor.run(speed/i)
#         wait(100)
#     right_motor.run(speed)
#     left_motor.run(speed)


def stage1():
    stage_1.run_angle(1000,180)
    stage_1.run_angle(1000,-180)
    Put_SL_Tensor("stage1", "STRING", "False")

def stage2():
    stage_2.run_angle(1000, 150)
    stage_2.run_angle(1000,-150)
    Put_SL_Tensor("stage2", "STRING", "False")

def stage3():
    stage_3.run_angle(1000,160)
    stage_3.run_angle(1000,-160)
    Put_SL_Tensor("stage3", "STRING", "False")

def main():
    Put_SL("Start28", "BOOLEAN", "True")
    while Get_SL("Start28") != "True":
    	print("Crying")
    	wait(100)
    Put_SL_Tensor("start", "STRING", "True")
    time.sleep(7)
    starter.run_angle(500,60)
    while Get_SL_Tensor("start") != "False":
        if Get_SL_Tensor("stage1") == "True":
            stage1()
        elif Get_SL_Tensor("stage2") == "True":
            stage2()
        elif Get_SL_Tensor("stage3") == "True":
            stage3()
        else:
            print("Idling..")
    Put_SL("Start28", "BOOLEAN", "False")
    Put_SL("Start29", "BOOLEAN", "True")
    print("done")

	# time.sleep(.5)
	# starter.run_angle(500,60)
	# time.sleep(2)



if __name__ == '__main__':
    main()
