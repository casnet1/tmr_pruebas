#!/usr/bin/env python3

from ev3dev2.sensor import *
import time 
from ev3dev2.motor import *
from ev3dev.ev3 import *

from alinear import *  
from busca_pared import *
from busca_color import *


from ev3dev.ev3 import *


us = UltrasonicSensor(INPUT_3) 
us.mode = 'US-DIST-CM'

  
#ya saber en que color esta, solo tiene que avanzar a la mitad del tubo
# cuando encuentre la tuberia que se posicione a la mitar


colors=('unknown','black','blue','green','yellow','red','white','brown')
#rojo mide 15 cm
# azul mide 20 cm
#amarilo mide 10cm
def mitad_tubo(color) :
        if color == 4:
          adelante(20,.5)
            
        if color == 5:
             adelante(20,.9)
            
        if color == 2:
            adelante(20,1.2)


def busca_tuberia(color) :
    sal = False

    while sal != True :    
        distance = us.value()
        print(distance)
        if (distance > 40):
          #  Leds.set_color(Leds.LEFT, Leds.RED)
            tank_drive.on(20,20)
            tank_drive.stop
            
        else:
           # Leds.set_color(Leds.LEFT, Leds.GREEN)
              
            mitad_tubo(color)
            sal = True

    Sound.beep()       
    Leds.set_color(Leds.LEFT, Leds.GREEN)


busca_tuberia(2)

  



