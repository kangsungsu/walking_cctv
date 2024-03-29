from ev3dev.ev3 import *
from time import sleep

class robot:
    def __init__(self):
        self.btn = Button() #혹시 모를 버튼 설정
        self.count = 0
    def launch(self):
        #모터 설정
        lm = LargeMotor('outC'); assert lm.connected
        rm = LargeMotor('outD'); assert rm.connected 

        us_f = UltrasonicSensor('in2'); assert us_f.connected
        us_r  =UltrasonicSensor('in4'); assert us_r.connected

        cs = ColorSensor('in3'); assert cs.connected
        
        us_f.mode = 'US-DIST-CM'
        us_r.mode = 'US-DIST-CM'

        cs.mode = 'COL-REFLECT'
        right_2 =us_r.value()
        sleep(0.5)
        while True:
            lm.run_forever(speed_sp = 100)
            rm.run_forever(speed_sp = 100)
                     
            #시작할 때, 센서들의 값 측정
            
    
            #쉬는 시간 0.5초 줘서 간격을 줌

            sleep(1)
            color = cs.value()
            right_1=right_2
            right_2 = us_r.value()
            front = us_f.value()
            
            angle  = right_1 -  right_2
           
            if color <15:
                flag=0
                while True:

                    color = cs.value()
                    while color>15:
                        sleep(0.5)
                        color=cs.value()
                        while color<15:
                            sleep(0.5)
                            color=cs.value()
                            while color>15:
                                flag=1
                                if flag==1:
                                    break
                            if flag==1:
                                break
                        if flag==1:
                            break
                    if flag==1:
                        break
                        
                        
                        
            
            if front <=70:
                print("front")
                lm.stop(stop_action = "brake")
                rm.stop(stop_action = "brake")

                sleep(0.5)
                lm.run_to_rel_pos(position_sp = -200, speed_sp = 300, stop_action = "brake")
                rm.run_to_rel_pos(position_sp = -200, speed_sp = 300, stop_action = "brake")              
            
                sleep(1)

                lm.run_to_rel_pos(position_sp = -190, speed_sp = 300, stop_action = "brake")
                rm.run_to_rel_pos(position_sp = 190, speed_sp = 300, stop_action = "brake")

                sleep(2)
               
            elif angle < -700:
                print("angle")
                lm.stop(stop_action = "brake")
                rm.stop(stop_action = "brake")

                sleep(1.5)
                lm.run_timed(time_sp = 800, speed_sp = 450)
                rm.run_timed(time_sp = 800, speed_sp = 450)

                sleep(1.5)

                lm.run_to_rel_pos(position_sp = 200, speed_sp = 300, stop_action = "brake")
                rm.run_to_rel_pos(position_sp = -200, speed_sp = 300, stop_action = "brake")
                
                sleep(2)


                lm.run_timed(time_sp = 400, speed_sp = 450)
                rm.run_timed(time_sp = 400, speed_sp = 450)

            elif (right_2 <=120 ) (angle>0):
                print("right1")

                lm.stop(stop_action = "brake")
                rm.stop(stop_action = "brake")

                rm.run_timed(time_sp = 250, speed_sp = 250)

                sleep(1.5)
            
            elif (right_2 >=300) and (angle <0):
                print("right2")
                lm.stop(stop_action = "brake")
                rm.stop(stop_action = "brake")

                lm.run_timed(time_sp = 325, speed_sp = 325)

                sleep(1.5)

   


              
                     
                                        
a = robot()
a.launch()
