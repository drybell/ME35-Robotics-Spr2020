#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import math
import ubinascii, ujson, urequests, utime

#set up the 3 motors
motor_claw = Motor(Port.C)
motor_elbow = Motor(Port.B)
motor_swivel = Motor(Port.A)

#API key for Systemlink
Key = 'xFXBfS_CWn75o_jHyTQWZ5TaU6GWD6sdUhUDfYVFMK'

#define functions for Systemlink
def SL_setup():
    urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
    headers = {"Accept":"application/json","x-ni-api-key":Key}
    return urlBase, headers

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

def Put_SL(Tag, Type, Value):
     urlBase, headers = SL_setup()
     urlValue = urlBase + Tag + "/values/current"
     propValue = {"value":{"type":Type,"value":Value}}
     try:
          reply = urequests.put(urlValue,headers=headers,json=propValue).text
     except Exception as e:
          print(e)        
          reply = 'failed'
     return reply

#reset all angles to 0 at the beginning of the program when the claw is at its initial position
motor_claw.reset_angle(0)
motor_elbow.reset_angle(0)
motor_swivel.reset_angle(0)

#return the arm from any position back to the "center" (initial) position
def return_to_center(motor_speed):
     motor_swivel.run_target(motor_speed,0)
     motor_elbow.run_target(motor_speed,0)

#arm goes to the position above the "small rails" cup and releases the piece into the cup
def position_s_rails(motor_speed):
     wait(2000)
     motor_claw.run_target(motor_speed, 10, stop_type = Stop.HOLD, wait=False)
     motor_elbow.run_target(motor_speed,-290, stop_type = Stop.BRAKE)
     motor_swivel.run_target(motor_speed,250)
     motor_claw.run_time(motor_speed, 1000)
     wait(200)
     motor_claw.run_target(motor_speed, 10, stop_type = Stop.HOLD, wait=False)
     return_to_center(motor_speed)

#arm goes to the position above the "large rails" cup and releases the piece into the cup
def position_l_rails(motor_speed):
     wait(2000)
     motor_claw.run_target(motor_speed, 10, stop_type = Stop.HOLD, wait=False)
     motor_elbow.run_target(motor_speed,-290, stop_type = Stop.BRAKE)
     motor_swivel.run_target(motor_speed,450)
     motor_claw.run_time(motor_speed, 1000)
     wait(200)
     motor_claw.run_target(motor_speed, 10, stop_type = Stop.HOLD, wait=False)
     return_to_center(motor_speed)

#arm goes to the position above the "joiners" cup and releases the piece into the cup
def position_joiners(motor_speed):
     wait(2000)
     motor_claw.run_target(motor_speed, 10, stop_type = Stop.HOLD, wait=False)
     motor_elbow.run_target(motor_speed,-290, stop_type = Stop.BRAKE)
     motor_swivel.run_target(motor_speed,600)
     motor_claw.run_time(600, 2000)
     wait(200)
     motor_claw.run_target(motor_speed, 10, stop_type = Stop.HOLD, wait=False)
     return_to_center(motor_speed)

#arm goes to the position above the "sticks" cup and releases the piece into the cup
def position_sticks(motor_speed):
     wait(2000)
     motor_claw.run_target(motor_speed, 10, stop_type = Stop.HOLD, wait=False)
     motor_elbow.run_target(motor_speed,-290, stop_type = Stop.BRAKE)
     motor_swivel.run_target(motor_speed,750)
     motor_claw.run_time(motor_speed, 1000)
     wait(200)
     motor_claw.run_target(motor_speed, 10, stop_type = Stop.HOLD, wait=False)
     return_to_center(motor_speed)


while True:

     #from systemlink, figure out what piece and the chosen speed of the arm
     piece = Get_SL('Piece type')
     motor_speed = int(Get_SL('Arm speed'))


     #if there is no piece, then arm does not move, if any other defined piece, move to that position
     if piece == 'nothing':
          wait(1500)
     elif piece == 'small rails':
          position_s_rails(motor_speed)
     elif piece == 'large rails':
          position_l_rails(motor_speed)
     elif piece == 'joiners':
          position_joiners(motor_speed)
     elif piece == 'sticks':
          position_sticks(motor_speed)
     
     wait(250)





