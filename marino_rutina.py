#!/usr/bin/env python3

from ev3dev2.sensor import *
import time 
from ev3dev2.motor import *
from ev3dev.ev3 import *

from alinear import *  
from busca_pared import *
from busca_color import *

colors=('unknown','black','blue','green','yellow','red','white','brown')
c=Sensor(address=INPUT_1, driver_name="ht-nxt-compass")


ariba = 47
abajo = 227
izq  = 317 
der = 137
#valueCompass= c.value()


tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

mA = LargeMotor('outA')
mB = LargeMotor('outB')

def adelante(speed, seconds):
    tank_drive.on_for_seconds(speed, speed, seconds, brake=True, block=True)
    tank_drive.stop
busca_pared()
alinea(izq)

busca_color(3)

adelante(20,6)
alinea(ariba)
busca_pared()
alinea(izq)
alinea(abajo)
tank_drive.stop

 #esta frente a los colores

        
