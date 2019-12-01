from ev3dev.ev3 import *
from time import sleep

us1 = UltrasonicSensor('in2'); assert us1.connected #Connection Sideus
us2 =UltrasonicSensor('in4'); assert us2.connected #Connection Frontus

lm = LargeMotor('outC'); assert lm.connected #connection rightMotor
rm = LargeMotor('outD'); assert rm.connected#connection leftMotor

us1.mode= 'US-DIST-CM' #calculating it as mm
us2.mode = 'US-DIST-CM' #calculating it as  mm 

while True:
    us1_a = us1.value() #measure the distance between front wall
    us2_a = us2.value() #measure the distance between side wall

    if us1_a <=70: #measure the distance between front wall and ev3
        lm.run_to_rel_pos(position_sp = -230, speed_sp = 300, stop_action= "brake")
        rm.run_to_rel_pos(position_sp = 230, speed_sp = 300, stop_action = "brake")

        sleep(3) #give time to move motors

#move forward
    lm.run_timed(time_sp = 600, speed_sp = 500)
    rm.run_timed(time_sp = 600, speed_sp = 500)
    
	
    sleep(1)

    lm.run_to_rel_pos(position_sp = 15, speed_sp = 300, stop_action = "brake")
    rm.run_to_rel_pos(position_sp = -15, speed_sp = 300, stop_action = "brake")

    sleep(0.5)

    us2_b = us2.value()

    if (us2_b - us2_a) > 700:#measure if ev3 has to turn right
        lm.run_to_rel_pos(position_sp = 230, speed_sp = 300, stop_action = "brake")
        rm.run_to_rel_pos(position_sp = -230, speed_sp = 300, stop_action = "brake")

        sleep(3)