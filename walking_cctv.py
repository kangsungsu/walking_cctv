from ev3dev.ev3 import *
from time import sleep

class robot:
    def __init__(self):
        self.btn = Button() #혹시 모를 버튼 설정

    def launch(self):
        #모터 설정
        lm = LargeMotor('outC'); assert lm.connected
        rm = LargeMotor('outD'); assert rm.connected 

        us_f = UltrasonicSensor('in2'); assert us_f.connected
        us_r  =UlratrasonicSensor('in4'); assert us_r.connected

        cs = ColorSensor('in3'); assert cs.connected
        
        us_f.mode = 'US-DIST-CM'
        us_r.mode = 'US-DIST-CM'

        cs.mode = 'COL-REFLECT'


        
        while True:
            lm.run_forever(speed_sp = 300)
            rm.run_forever(speed_sp = 300)
        
            #시작할 때, 센서들의 값 측정
            right_1 =us_r.value()
            color = cs.value()

            #쉬는 시간 1초 줘서 간격을 줌

            sleep(1)

            right_2 = us_r.value()
            front = us_f.value()
            angle  = right_1 -  right_2
            if front <=40:
                lm.stop(stop_action = "brake")
                rm.stop(stop_action = "brake")

                sleep(0.5)
                lm.run_to_rel_pos(position_sp = -200, speed_sp = 300, stop_action = "brake")
                rm.run_to_rel_pos(position_sp = -200, speed_sp = 300, stop_action = "brake")              
            
                sleep(1)

                lm.run_to_rel_pos(position_sp = +175, speed_sp = 300, stop_action = "brake")
                rm.run_to_rel_pos(position_sp = -175, speed_sp = 300, stop_action = "brake")

                sleep(2)

            elif angle <=-500:
                lm.stop(stop_action = "brake")
                rm.stop(stop_action = "brake")

                sleep(0.5)

                lm.run_to_rel_pos(position_sp = 300, speed_sp = 300, stop_action = "brake")
                rm.run_to_rel_pos(position_sp = -300, speed_sp = 300, stop_action = "brake")
                
                sleep(2)

            elif (right_2 <=70 )and (angle >0):
                lm.stop(stop_action = "brake")
                rm.stop(stop_action = "brake")

                rm.run_timed(time_sp = 300, speed_sp = 150)
                sleep(0.5)
            
            elif (right_2 >=200) and (angle <0):
                lm.run_timed(time_sp = 300, speed_sp = 150)
                sleep(0.5)

            


a = robot()
a.launch()

            
            

            
            



        
