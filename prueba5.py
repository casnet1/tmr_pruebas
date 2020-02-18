import bluetooth
from ev3dev2.motor import LargeMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep

m1=LargeMotor("outA")
m2=LargeMotor("outB")


m1.on_for_degrees(SpeedRPM(170),1)
sleep(6)








"""
bd_addr = "00:17:EC:EE:82:EA"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("me movi (3,2)")

sock.close()
"""