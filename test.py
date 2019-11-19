from ev3dev.ev3 import *
from time import sleep

us2 = UltrasonicSensor('in4'); assert us2.connected
us2.mode = "US-DIST-CM"

lm = LargeMotor('outC'); assert lm.connected
rm = LargeMotor('outD'); assert rm.connected

while True:
    first_us2_value = us2.value()
    print("1:")
    print(first_us2_value)
    lm.run_timed(time_sp = 1000, speed_sp = 300)
    rm.run_timed(time_sp = 1000, speed_sp = 300)
        
    sleep(1)
    second_us2_value = us2.value() #mm
    print("2")
    print(second_us2_value)
    if first_us2_value <=70:
        angle = first_us2_value - second_us2_value
        
        if angle >0:
           rm.run_timed(time_sp=300,speed_sp=150)  
    elif first_us2_value >=200:
        angle = first_us2_value -  second_us2_value
        
        if angle <0:
            
           
            lm.run_timed(time_sp=300, speed_sp=300)
            sleep(0.5)
    else:
        print("go")
       
            
            
