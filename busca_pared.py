from ev3dev2.sensor import *
import time 
from ev3dev2.motor import *
from ev3dev.ev3 import *

from alinear import *  


colors=('unknown','black','blue','green','yellow','red','white','brown')
c=Sensor(address=INPUT_1, driver_name="ht-nxt-compass")



#valueCompass= c.value()


tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

mA = LargeMotor('outA')
mB = LargeMotor('outB')

def adelante(speed, seconds):
    tank_drive.on_for_seconds(speed, speed, seconds, brake=True, block=True)
    tank_drive.stop
# 47,tierra mover a 13
abajo = 13



#alinea(abajo)  

def busca_pared():
    us = UltrasonicSensor() 
    us.mode = 'US-DIST-CM'

    distance = us.value()

    fondo = False
    ban = 1
    
    while True :
        distance = us.value()
        print(distance)
        if distance >= 40:
            tank_drive.on(20,20)
            tank_drive.stop
        else:
            tank_drive.stop
            '''adelante(-20,1)
            tank_drive.stop'''
            print('Estas en la pared')
            break
    tank_drive.stop
    tank_drive.off
    return 
