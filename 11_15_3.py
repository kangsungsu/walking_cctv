import ev3dev.ev3 as ev3
from time import sleep
from math import *


us1 = ev3.UltrasonicSensor('in4'); assert us1.connected
#cs.mode = 'COL-REFLECT'
us1.mode = 'US-DIST-CM'

lm = ev3.LargeMotor('outC'); assert lm.connected
rm = ev3.LargeMotor('outD'); assert rm.connected



#setting for init value

first_us_value = us1.value()//10

count =0
'''
while first_us_value >=2 and first_us_value<=4:
    lm.run_timed(time_sp = 3000, speed_sp = 500)
    rm.run_timed(time_sp = 3000, speed_sp = 500)

    sleep(0.5)
    count +=1
    if count==3:
        break
    
'''
while True:

    first_us_value = us1.value()/10
    print(first_us_value)

    if first_us_value >=15:
        #lm.run_to_rel_pos(position_sp = 50, speed_sp = 300, stop_action = "hold")
        lm.run_timed(time_sp=300, speed_sp=300)
        sleep(0.05)
        lm.run_timed(time_sp =50, speed_sp = 100)
        rm.run_timed(time_sp = 50, speed_sp = 100)

        sleep(0.5)
    elif first_us_value<=4:
        rm.run_timed(time_sp=100, speed_sp=100)
        sleep(0.5)
    else:
        lm.run_timed(time_sp = 1000, speed_sp = 200)
        rm.run_timed(time_sp = 1000, speed_sp = 200)
	                                 
                

                

                
        
        
