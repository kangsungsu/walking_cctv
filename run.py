from ev3dev.ev3 import *
from time import sleep

lm = LargeMotor('outC'); assert lm.connected
rm = LargeMotor('outD'); assert rm.connected 

lm.run_forever(speed_sp = 300)
rm.run_forever(speed_sp = 300)
