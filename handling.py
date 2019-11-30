from ev3dev.ev3 import *
from time import sleep
    
lm = LargeMotor('outC'); assert lm.connected
rm = LargeMotor('outD'); assert rm.connected 

direct=int(input("방향각을 입력하세요(왼쪽기준"))
direct=direct*20/9
lm.stop(stop_action = "brake")
rm.stop(stop_action = "brake")

lm.run_to_rel_pos(position_sp = -200, speed_sp = 300, stop_action = "brake")
rm.run_to_rel_pos(position_sp = -200, speed_sp = 300, stop_action = "brake")              
            
sleep(1)

lm.run_to_rel_pos(position_sp = direct, speed_sp = 300, stop_action = "brake")
rm.run_to_rel_pos(position_sp = direct, speed_sp = 300, stop_action = "brake")

                        
        
