#!/usr/bin/env python3

from ev3dev2.sensor import *
import time 
from ev3dev2.motor import *
from ev3dev.ev3 import *

from alinear import *  


c=Sensor(address=INPUT_1, driver_name="ht-nxt-compass")

#valueCompass= c.value()


tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

mA = LargeMotor('outA')
mB = LargeMotor('outB')

def adelante(speed, seconds):
    tank_drive.on_for_seconds(speed, speed, seconds, brake=True, block=True)
    tank_drive.stop
alinea(45)
i = 45    
while True:
    adelante(20,5)
    i = (90 + i) % 360
    alinea(i)
