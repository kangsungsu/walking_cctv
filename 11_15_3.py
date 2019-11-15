import ev3dev3.ev3 as ev3
from time import sleep
from math import *


us1 = ev3.UltrasonicSensor('in4'); assert us1.connected
cs.mode = 'COL-REFLECT'
us.mode = 'US-DIST-CM'

lm = ev3.LargeMotor('outC'); assert lm.connected
rm = ev3.LargeMotor('outD'); assert rm.connected

#setting for init value

first_us_value = us1.value()//10
print(first_us_value)
                                  
                

                

                
        
        
