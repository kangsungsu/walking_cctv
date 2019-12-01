from ev3dev.ev3 import *
import time as t

print("hi")

class robot:
    def __init__(self):
        self.btn = Button()
        self.shut_down = False


    def launch(self):
        #센서와 모터 설정 확인 부분        
        cs = ColorSensor('in3');         assert cs.connected #컬러센서 연결 확인
        us1 = UltrasonicSensor('in2);       assert us1.connected    #초음파 연결 확인
        us2 = UltrasonicSensor('in4);       assert us2.connected    #초음파2 연결 확인
        cs.mode = 'COL-REFLECT' #반사광 강도 모드 설정
        us.mode = 'US-DIST-CM' #cm로 거리 측정

        lm = LargeMotor('outB');        assert lm.connected #연결되었나 확인
        rm = LargeMotor('outC');        assert rm.connected #연결되었나 확인
        
        while not self.shut_down:
        
            first_us2_value = us2.value() #mm 단위로 계산
            lm.run_timed(time_sp = 1000, speed_sp = 300)
            rm.run_timed(time_sp = 1000, speed_sp = 300)
        
            lm.stop(stop_action = "brake")
            rm.stop(stop_action = "brake")
        
            lm.wait_while('running')
            rm.wait_while('running')
     
            second_us2_value = us2.value() #mm 단위로 계산
        
            if first_us2_value <=70:
                angle = first_us2_value - second_us2_value
            
                if angle >0:
                    lm.run_to_rel_pos(position_sp = -100, speed_sp = 100, stop_action = "brake")
                    rm.run_to_rel_pos(position_sp = -100, speed_sp = 100, stop_action = "brake")
                
            elif first_us2_value >=200:

                angle = first_us2_value - second_us2_value #두 값을 비교해서 꺾어야하는 지 판단

            
                if angle < 0:
                    lm.run_to_rel_pos(position_sp = 100, speed_sp = 100, stop_action = "brake")
                    rm.run_to_rel_pos(position_sp = 100, speed_sp = 100, stop_action = "brake")
                
            else:
                print("go")
            
            if self.btn.down:
                print("End Program")
                self.shut_down = True
       

a = robot()
a.launch()
            
        
        