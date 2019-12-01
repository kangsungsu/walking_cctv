from ev3dev.ev3 import *
from time import sleep


cs = ColorSensor('in3'); assert cs.connected


lm = LargeMotor('outC'); assert lm.connected
rm = LargeMotor('outD'); assert rm.connected

cs.mode = 'COL-REFLECT'

count = 0



while True:
    lm.run_timed(time_sp = 300, speed_sp = 300)
    rm.run_timed(time_sp= 300, speed_sp = 300)
    
    cs_a = cs.value()
    print(cs_a)
    
    if cs_a <15:
        while True:
            lm.run_timed(time_sp = 300, speed_sp = 300)
            rm.run_timed(time_sp = 300, speed_sp = 300)

            sleep(1)
            cs_b = cs.value()
            print(cs_b)
            if cs_b <15:
                lm.run_to_rel_pos(position_sp = 360, speed_sp = 900, stop_action = "brake")
                rm.run_to_rel_pos(position_sp = -360, speed_sp = 900, stop_action = "brake")
                count+=1
                break
    if count == 1:
        break
    


    if count ==1:
        break
