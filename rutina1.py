#!/usr/bin/env python3

 ##################         SEARCH ROBOT   #######################
from ev3dev2.motor import *
#from ev3dev.ev3 import *
from time import sleep



from ev3dev.ev3 import *


tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

mA = LargeMotor('outA')
mB = LargeMotor('outB')


###################3            FUCTIONS        ################
def adelante(pot,sec):
    #tank_drive.on_for_seconds(pot,pot,sec)
    tank_drive.on(50,50)

def atras(pot,sec):
    tank_drive.on_for_seconds(-pot,-pot,sec)
    
def vueltaD(pot,sec):
    tank_drive.on_for_seconds(-pot,pot,sec)

def vueltaI(pot,sec):
    tank_drive.on_for_seconds(pot,-pot,sec)
      





#################            RUN    ##################

#buscar colores
# Connect EV3 color and touch sensors to any sensor ports
cl = ColorSensor() 


# Put the color sensor into COL-COLOR mode.
cl.mode='COL-COLOR'

colors=('unknown','black','blue','green','yellow','red','white','brown')
while  cl.value() != 2:    # Stop program by color is blue
    adelante(3,3)
    print(colors[cl.value()])
    #Sound.speak(colors[cl.value()]).wait()
tank_drive.stop()
Sound.beep()



