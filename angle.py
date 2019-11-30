from ev3dev.ev3 import *
from time import sleep
    
lm = LargeMotor('outC'); assert lm.connected
rm = LargeMotor('outD'); assert rm.connected 

            
sleep(4)

lm.run_to_rel_pos(position_sp = -100, speed_sp = 300, stop_action = "brake")
rm.run_to_rel_pos(position_sp = 100, speed_sp = 300, stop_action = "brake")
sleep(4)
lm.run_to_rel_pos(position_sp = -200, speed_sp = 300, stop_action = "brake")
rm.run_to_rel_pos(position_sp = 200, speed_sp = 300, stop_action = "brake")

sleep(4)
lm.run_to_rel_pos(position_sp = -300, speed_sp = 300, stop_action = "brake")
rm.run_to_rel_pos(position_sp = 300, speed_sp = 300, stop_action = "brake")

sleep(4)
lm.run_to_rel_pos(position_sp = -400, speed_sp = 300, stop_action = "brake")
rm.run_to_rel_pos(position_sp = 400, speed_sp = 300, stop_action = "brake")

sleep(4)
lm.run_to_rel_pos(position_sp = -500, speed_sp = 300, stop_action = "brake")
rm.run_to_rel_pos(position_sp = 500, speed_sp = 300, stop_action = "brake")

sleep(4)
lm.run_to_rel_pos(position_sp = -600, speed_sp = 300, stop_action = "brake")
rm.run_to_rel_pos(position_sp = 600, speed_sp = 300, stop_action = "brake")

sleep(4)
lm.run_to_rel_pos(position_sp = -700, speed_sp = 300, stop_action = "brake")
rm.run_to_rel_pos(position_sp = 700, speed_sp = 300, stop_action = "brake")

sleep(4)
lm.run_to_rel_pos(position_sp = -800, speed_sp = 300, stop_action = "brake")
rm.run_to_rel_pos(position_sp = 800, speed_sp = 300, stop_action = "brake")
sleep(4)
lm.run_to_rel_pos(position_sp = -900, speed_sp = 300, stop_action = "brake")
rm.run_to_rel_pos(position_sp = 900, speed_sp = 300, stop_action = "brake")
                        
        
