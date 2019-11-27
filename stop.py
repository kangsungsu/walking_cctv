from ev3dev.ev3 import *
lm = LargeMotor('outC'); assert lm.connected
rm = LargeMotor('outD'); assert rm.connected 
lm.stop(stop_action = "brake")
rm.stop(stop_action = "brake")
