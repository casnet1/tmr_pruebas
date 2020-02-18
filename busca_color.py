from ev3dev2.sensor import *
import time 
from ev3dev2.motor import *
from ev3dev.ev3 import *

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

mA = LargeMotor('outA')
mB = LargeMotor('outB')

def adelante(speed, seconds):
    tank_drive.on_for_seconds(speed, speed, seconds, brake=True, block=True)
    tank_drive.stop
def busca_color(col):
    colors=('unknown','black','blue','green','yellow','red','white','brown')
    c=Sensor(address=INPUT_1, driver_name="ht-nxt-compass")
    cl = ColorSensor()
    cl.mode = 'COL-COLOR'

    while cl.value() != col:
        #print(colors[cl.value()]) 
        tank_drive.on(20,20)
        tank_drive.stop
    adelante(20,3)
    #alinea(241)
    
    