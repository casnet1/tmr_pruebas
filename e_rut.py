#!/usr/bin/env python3

from ev3dev2.sensor import *
import time 
from ev3dev2.motor import *
from ev3dev.ev3 import *

from alinear import *  
from busca_pared import *
from busca_color import *



c=Sensor(address=INPUT_1, driver_name="ht-nxt-compass")



#valueCompass= c.value()


tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

mA = LargeMotor('outA')
mB = LargeMotor('outB')

def adelante(speed, seconds):
    tank_drive.on_for_seconds(speed, speed, seconds, brake=True, block=True)
    tank_drive.stop

#alinea(45)  
"""
ariba = 47
abajo = 227
izq  = 317 
der = 137
"""

#robot tierra
ariba = 20
abajo = 200
izq  = 290 
der = 180



us = UltrasonicSensor() 
us.mode = 'US-DIST-CM'

distance = us.value()

fondo = False

   
busca_pared()
alinea(der)
busca_color(1)
adelante(20,1)

alinea(270)
busca_color(2)

    

    
    

            
        
