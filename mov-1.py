#!/usr/bin/env python3


import time 
from ev3dev2.motor import *
from ev3dev.ev3 import *


tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

mA = LargeMotor('outA')
mB = LargeMotor('outB')


def adelante(pot):
    tank_drive.on(pot,pot)

def atras(pot):
    tank_drive.on(-pot,-pot)
    
def vueltaD(pot):
    tank_drive.on(-pot,pot)

def vueltaI(pot):
    tank_drive.on(pot,-pot)


adelante(50)
time.sleep(3)
mA.stop

atras(50)
time.sleep(3)
mA.stop

vueltaD(50)
time.sleep(3)
mA.stop

vueltaI(50)
time.sleep(3)
mA.stop


print(mA.count_per_rot)
print(mB.count_per_rot)
print(mA.max_speed)

tank_drive.on_for_rotations(50, 75, 10)
