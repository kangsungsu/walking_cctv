#!/usr/bin/env python3

from ev3dev.ev3 import *
import time as t

class robot:
    def __init__(self):
        self.btn = ev3.Button()
        self.shut_down = False


    def launch(self):
        #센서와 모터 설정 확인 부분        
        cs = ev3.ColorSensor();         assert cs.connected #컬러센서 연결 확인
        us1 = ev3.UltrasonicSensor();       assert us1.connected    #초음파 연결 확인
        us2 = ev3.UltrasonicSensor();       assert us2.connected    #초음파2 연결 확인
        cs.mode = 'COL-REFLECT' #반사광 강도 모드 설
        us.mode = 'US-DIST-CM' #cm로 거리 측정

        lm = ev3.LargeMotor('outB');        assert lm.connected #연결되었나 확인
        rm = ev3.LargeMotor('outC');        assert rm.connected #연결되었나 확인

