from ev3dev2.motor import *



"""
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

# drive in a turn for 5 rotations of the outer motor
# the first two parameters can be unit classes or percentages.
tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(75), 10)

# drive in a different turn for 3 seconds
tank_drive.on_for_seconds(SpeedRPS(1.5), SpeedRPS(1.5), 3)

m = LargeMotor(OUTPUT_B)

cuenta = m.full_travel_count

print(cuenta)

"""
"""
#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

mB = LargeMotor('outB')
mA = LargeMotor('outA')
mA.run_to_rel_pos(position_sp=360, speed_sp=900, stop_action="hold")

sleep(4)
mA.stop()


"""

m = LargeMotor(OUTPUT_A)
m.on_for_rotations(SpeedPercent(25), 5)

print(m.duty_cycle)
