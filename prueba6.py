#!/usr/bin/env python3

import time 
from ev3dev2.motor import *
from ev3dev.ev3 import *



tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

mA = LargeMotor('outA')
mB = LargeMotor('outB')


starting_point = time.time()
time_final=0


def adelante(pot,sec):
    #tank_drive.on_for_seconds(pot,pot,sec)
    tank_drive.on(pot,pot)

def atras(pot,sec):
    #tank_drive.on_for_seconds(-pot,-pot,sec)
    tank_drive.on(-pot,-pot)
    
def vueltaD(pot,sec):
    #tank_drive.on_for_seconds(-pot,pot,sec)
    tank_drive.on(-pot,pot)
def vueltaI(pot,sec):
    #tank_drive.on_for_seconds(pot,-pot,sec)
    tank_drive.on(pot,-pot)




cl = ColorSensor() 


cl.mode='COL-COLOR'

colors=('unknown','black','blue','green','yellow','red','white','brown')
while  cl.value() != 2:    
    adelante(3,3)
    print(colors[cl.value()])
    #Sound.speak(colors[cl.value()]).wait()
tank_drive.stop()
time_final=time.time()
Sound.beep()


"""
elapsed_time = time_final - starting_point
elapsed_time_int = int(elapsed_time)

elapsed_time_minutes = elapsed_time_int / 60 
elapsed_time_seconds = elapsed_time_int % 60

print(elapsed_time_minutes)
print(elapsed_time_seconds)
time.sleep(6)
"""


