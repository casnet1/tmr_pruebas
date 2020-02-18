from ev3dev2.sensor import *
c=Sensor(address=INPUT_2, driver_name="ht-nxt-compass")
print(c.address)
value= c.value()
print(value)