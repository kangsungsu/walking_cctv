from ev3dev.ev3 import *
from time import sleep
lm = LargeMotor('outC'); assert lm.connected
rm = LargeMotor('outD'); assert rm.connected
cs = ColorSensor('in3'); assert cs.connected
lm.run_forever(speed_sp = 50)
rm.run_forever(speed_sp = 50)
while True:
    us_f = UltrasonicSensor('in2'); assert us_f.connected
    us_r  =UltrasonicSensor('in4'); assert us_r.connected
    front = us_f.value()
    right = us_r.value()
    color=cs.value()
    print("\nfront")
    print(front)
    
    print("\nright")
    print(right)
    
    print("\ncolor")
    print(color)
    