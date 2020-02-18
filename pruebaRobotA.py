#!/usr/bin/env python3

import time 
from ev3dev2.motor import *
from ev3dev.ev3 import *


tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

mA = LargeMotor('outA')
mB = LargeMotor('outB')


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


def sigueAlNegro():
    if(cl.value() == negro) 
        vueltaD()
    else
        vueltaI()



cl = ColorSensor() 
cl.mode='COL-COLOR'
colors=('unknown','black','blue','green','yellow','red','white','brown')




do{
adelante(50,4)

switch (cl.value()) :

case 1: sigueAlNegro()

case 3: encuentraAlNegro()

}while(ultrasonic < 80)