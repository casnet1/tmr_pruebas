#!/usr/bin/env python3

'''
Prueba con el robot TIERRA  

MediumMotor = Mecanismo de carga y descarga
LargeMotor1 = Llanta derecha
LargeMotor2 = Llanta izquierda
CompassSensor


'''
from ev3dev2.sensor import *

from ev3dev2.motor import MediumMotor, LargeMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
#from ev3dev2.sensor.lego import UltrasonicSensor
#from ev3dev2.button import Button
from ev3dev2.sound import Sound
from time import sleep

mm = MediumMotor()
#us = UltrasonicSensor()
#btn = Button()
lm1 = LargeMotor(address = INPUT_D)
lm2 = LargeMotor(address = INPUT_c)
sound = Sound()
cs =Sensor(address=INPUT_2, driver_name="ht-nxt-compass")

sound.beep()
value= c.value()
print(value)


#cm = us.distance_centimeters_ping
#print(cm)
sleep(1)
'''
This will run the large motor at 50% of its
rated maximum speed of 1050 deg/s.
50% x 1050 = 525 deg/s
'''
sound.beep()
lm1.on_for_seconds(speed = -60, seconds=2)
lm2.on_for_seconds(speed = 60, seconds=2)
value= c.value()
print(value)
sleep(1)

'''
speed and seconds are both POSITIONAL
arguments which means
you don't have to include the parameter names as
long as you put the arguments in this order 
(speed then seconds) so this is the same as
the previous command:
'''
sound.beep()
lm1.on_for_seconds(50, 2)
lm2.on_for_seconds(-50, 2)
value= c.value()
print(value)
sleep(1)

'''
This will run at 500 degrees per second (DPS).
You should be able to hear that the motor runs a
little slower than before.
'''