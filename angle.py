from ev3dev.ev3 import *
from time import sleep
    
lm = LargeMotor('outC'); assert lm.connected
rm = LargeMotor('outD'); assert rm.connected 

            
sleep(4)

lm.run_to_rel_pos(position_sp = -200, speed_sp = 150, stop_action = "brake")
rm.run_to_rel_pos(position_sp = 200, speed_sp = 150, stop_action = "brake")
sleep(4)
lm.run_to_rel_pos(position_sp = -200, speed_sp = 300, stop_action = "brake")
rm.run_to_rel_pos(position_sp = 200, speed_sp = 300, stop_action = "brake")

sleep(4)
lm.run_to_rel_pos(position_sp = -200, speed_sp = 450, stop_action = "brake")
rm.run_to_rel_pos(position_sp = 200, speed_sp = 450, stop_action = "brake

sleep(4)
lm.run_to_rel_pos(position_sp = -200, speed_sp = 600, stop_action = "brake")
rm.run_to_rel_pos(position_sp = 200, speed_sp = 600, stop_action = "brake")

sleep(4)
lm.run_to_rel_pos(position_sp = -200, speed_sp = 750, stop_action = "brake")
rm.run_to_rel_pos(position_sp = 200, speed_sp = 750, stop_action = "brake")

sleep(4)
lm.run_to_rel_pos(position_sp = -200, speed_sp = 900, stop_action = "brake")
rm.run_to_rel_pos(position_sp = 200, speed_sp = 900, stop_action = "brake")

sleep(4)
lm.run_to_rel_pos(position_sp = -400, speed_sp = 1150, stop_action = "brake")
rm.run_to_rel_pos(position_sp = 400, speed_sp = 1150, stop_action = "brake")

sleep(4)
lm.run_to_rel_pos(position_sp = -400, speed_sp = 1300, stop_action = "brake")
rm.run_to_rel_pos(position_sp = 400, speed_sp = 1300, stop_action = "brake")
                        
        
