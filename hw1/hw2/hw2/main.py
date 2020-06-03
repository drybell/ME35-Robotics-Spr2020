#!/usr/bin/env pybricks-micropython

# G3tH4CK3DM4T3

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from time import sleep 
import ubinascii, ujson, urequests, utime

#10x10x10cm cube built out of legos
# full steam ahead, maneuver to ball, full steam back

Key = 'xFXBfS_CWn75o_jHyTQWZ5TaU6GWD6sdUhUDfYVFMK'

def Get_SL(Tag):
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

left = Motor(Port.A)
right = Motor(Port.C)
hook = Motor(Port.B)

counter = 0
previous_value = "false"
while True:
    hook_value = Get_SL('Hook')

    if hook_value == "true" and previous_value == "false":
        counter += 1
        hook.run_time(-500, 1800)
        previous_value = "true"
    elif hook_value == "false" and previous_value == "true": 
        counter += 1
        hook.run_time(500, 1800)
        previous_value = "false"
    
    left_value = Get_SL('Left')
    left.run(float(left_value))
    right_value = Get_SL('Right')
    right.run(float(right_value))
