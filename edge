from ev3dev.ev3 import *
from time import sleep

us1 = UltrasonicSensor('in2'); assert us1.connected #Connection Sideus
us2 =UltrasonicSensor('in4'); assert us2.connected #Connection Frontus

lm = LargeMotor('outC'); assert lm.connected #connection rightMotor
rm = LargeMotor('outD'); assert rm.connected#connection leftMotor

us1.mode= 'US-DIST-CM' #calculating it as mm
us2.mode = 'US-DIST-CM' #calculating it as  mm 

lm.run_forever(speed_sp = 450)
rm.run_forever(speed_sp = 450)
while True:
    us1_a = us1.value()
    us2_a = us2.value()
    
    sleep(1)
    
    us2_b = us2.value()
    
    if us1_a <70:
        lm.stop(stop_action = "brake")
        rm.stop(stop_action = "brake")
        
        sleep(0.5)
        lm.run_to_rel_pos(position_sp = -200, speed_sp = 200, stop_action = "brake")
        rm.run_to_rel_pos(position_sp = -200, speed_sp =200, stop_action = "brake")        

        sleep(1)


        lm.run_to_rel_pos(position_sp = -175, speed_sp = 300, stop_action = "brake")
        rm.run_to_rel_pos(position_sp = +175, speed_sp = 300, stop_action = "brake")
        
        sleep(2)
        
        lm.run_forever(speed_sp = 450)
        rm.run_forever(speed_sp = 450)
        
    elif (us2_b - us2_a) > 500:
        lm.stop(stop_action = "brake")
        rm.stop(stop_action = "brake")
        
        sleep(0.5)
        
        lm.run_to_rel_pos(position_sp = 300, speed_sp = 300, stop_action = "brake")
        rm.run_to_rel_pos(position_sp = -300, speed_sp = 300, stop_action = "brake")
        
        sleep(2)
        
        lm.run_forever(speed_sp = 450)
        rm.run_forever(speed_sp = 450)
        
        
