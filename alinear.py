#!/usr/bin/env python3

from ev3dev2.sensor import *
import time 
from ev3dev2.motor import *
from ev3dev.ev3 import *




c=Sensor(address=INPUT_1, driver_name="ht-nxt-compass")

#valueCompass= c.value()


tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

mA = LargeMotor('outA')
mB = LargeMotor('outB')


'''def adelante(pot):
    tank_drive.on(pot,pot)

def atras(pot):
    tank_drive.on(-pot,-pot)
'''    
def vueltaD(pot):
    tank_drive.on(-pot,pot)

def vueltaI(pot):
    tank_drive.on(pot,-pot)
    
'''def vueltaD(pot):
    tank_drive.on_for_degrees(left_speed, right_speed, degrees, brake=True, block=True)
def vueltaD(pot):
    tank_drive.on_for_degrees(left_speed, right_speed, degrees, brake=True, block=True)'''
#print(c.address)
def how_many(value): #puse esta funcion para que le de poca potencia al acercarse a los 45
    if value < 60:   #grados de cercania a alphan 
        return 5 #potencia del motor
    if value < 100:
        return 15
    if value < 360:
        return 20
def ok(value, alpha): # si ya esta en el rango que ya salga del while
    if value > alpha - 4 and value < alpha + 4:
        return True
    return False

def alinea(alpha):
    ban =  False
    _which = 0 # variable para saber la vuelta derecha o izquierda
    err = 0     # aun no sirve esta variable
    valueCompass= c.value()
    print(valueCompass)
    while ok(valueCompass, alpha) == False:
        ban = True
        valueCompass= c.value()
        print(valueCompass) 

        if valueCompass < alpha - 1 or valueCompass > alpha + 179:
            if(valueCompass < alpha-1):
                pot = alpha - valueCompass   #grado que que pasa a la funcion para bajar la velocidad 
            else:
                pot = 360 - valueCompass + alpha
            vueltaD(how_many(pot))
            _which = 1
            tank_drive.stop
            
        # tank_drive.stop
        elif valueCompass > alpha + 3 and valueCompass < alpha + 179 :
            vueltaI(how_many(valueCompass - alpha) ) #el modulo lo use porque me muevo dentro de 180 grados ya sea izq o der
            _which = 2
            tank_drive.stop
    
    #corrige lo que se paso, solo si entro al while
    if ban == True:
        if _which == 1:
            vueltaI(3)
        else:
            vueltaD(3)
    tank_drive.stop
    return


#alinea(315) #por ahora solo funciona para 45, lo arreglare 
#y hay un rango de error de +4 y -4 depende del giro
print("****************************************************")




        