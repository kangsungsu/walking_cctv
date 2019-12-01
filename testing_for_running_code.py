from ev3dev.ev3 import *
import time as sleep

us2 = UltrasonicSensor('in4'); assert connected
us2.mode = "US-DIST-CM"

lm = LargeMotor('outC');
rm = LargeMotor('outD');

while True:
    first_us2_value = us2.value()
    lm.run_timed(time_sp = 1000, speed_sp = 300)
    rm.run_timed(time_sp = 1000, speed_sp = 300)
        
    lm.stop(stop_action = "brake")
    rm.stop(stop_action = "brake")
        
    lm.wait_while('running')
    rm.wait_while('running')
     
    sleep(0.3)
    
    second_us2_value = us2.value() #mm 단위로 계산
    
    if first_us_value <=70:
        angle = first_us2_value - second_us2_value
        
        if angle >0:
            lm.run_to_rel_pos(position_sp = -30, speed_sp = 30, stop_action = stop_action)
            rm.run_to_rel_pos(position_sp = -30, speed_sp = 30, stop_action = stop_action)
            
    elif first_us2_value >=200:
        angle = first_us2_value -  second_us2_value
        
        if angle <0:
            lm.run_to_rel_pos(position_sp = 30, speed_sp = 30, stop_action = stop_action)
            rm.run_to_rel_pos(position_sp = 30, speed_sp = 30, stop_action = stop_action)
            
    else:
        print("go")
       
            
            
