import ev3dev3.ev3 as ev3
from time import sleep
from math import *
class robot:
    def __init__(self):
        self.btn = Button()
        self.shut_down = False

    def launch(self):
        #cs = ev3.ColorSensor(); assert cs.connected
        in4 = ev3.UltrasonicSensor(); assert in4.connected
        #us2 =  ev3.UltrasonicSensor(); assert us2.connected

        #cs.mode = 'COL-REFLECT'
        in4.mode = 'US-DIST-CM'

        lm = ev3.LargeMotor('outC'); assert lm.connected
        rm = ev3.LargeMotor('outD'); assert rm.connected

        #setting for init value

        #first_us_value = us1.value()//10
        #second_us_value = us2.value()//10


        while not run_value:
            lm.run_timed(time_sp = 1000, speed_sp = 0)
            rm.run_timed(time_sp= 1000, speed_sp = 0)

            lm.stop(stop_action = "brake")
            rm.stop(stop_action = "brake")

            lm.wait_while('running')
            rm.wait_while('running')

            sleep(0.1)

            #check the distance between us2 and wall
            
            now_us1 = in4.value()//10
            #now_us2  us2.value()//10
            #now_cs = cs.value()//10

            if now_us1 <=4:
                rm.run_to_rel_pos(position_sp = -20, speed_sp = 300, stop_action = "brake")
                sleep(0.1)
            elif now_us1 >=10:
                lm.run_to_rel_pos(position_sp = 20, speed_sp = 300, stop_action = "brake")
                sleep(0.1)
                
            else:
                print("go")
                sleep(0.1)

          
            if not self.btn.down:
                print("End Program")
                self.shut_down = True

go = robot()
go.launch()

            


            

                



                                  
                

                

                
        
        
