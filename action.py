from adafruit_servokit import ServoKit
import time

class action():

    def __init__(self):
        self.kit = ServoKit(channels=16)
        self.kit.servo[0].actuation_range = 359
        self.kit.servo[1].actuation_range = 359
        self.kit.servo[2].actuation_range = 359
        self.kit.servo[3].actuation_range = 359
        self.kit.servo[4].actuation_range = 359
        self.kit.servo[5].actuation_range = 359

        #setup servo position feedback 
        self.servo0_pos = 230
        self.servo1_pos = 30
        self.servo2_pos = 250
        self.servo3_pos = 243
        self.servo4_pos = 94
        self.servo5_pos = 180



        #setup servo limits
        self.servo0_hi_lim = 270
        self.servo0_lo_lim = 90
        self.servo1_hi_lim = 180
        self.servo1_lo_lim = 20
        self.servo2_hi_lim = 340
        self.servo2_lo_lim = 20
        self.servo3_hi_lim = 359
        self.servo3_lo_lim = 220
        self.servo4_hi_lim = 180
        self.servo4_lo_lim = 0
        self.servo5_hi_lim = 180
        self.servo5_lo_lim = 0




        #set movement rate
        self.movedeg = 10
        #reset robot position
        self.reset_robot()


    def reconnect(self):
        self.kit = ServoKit(channels=16)
        self.kit.servo[0].actuation_range = 359
        self.kit.servo[1].actuation_range = 359
        self.kit.servo[2].actuation_range = 359
        self.kit.servo[3].actuation_range = 359
        self.kit.servo[4].actuation_range = 359
        self.kit.servo[5].actuation_range = 359





    def reset_robot(self):
        self.kit.servo[0].angle = int(self.servo0_pos)
        self.kit.servo[1].angle = int(self.servo1_pos)
        self.kit.servo[2].angle = int(self.servo2_pos)
        self.kit.servo[3].angle = int(self.servo3_pos)
        self.kit.servo[4].angle = int(self.servo4_pos)
        self.kit.servo[5].angle = int(self.servo5_pos)


    def move_robot_arm(self,controlNum):

        self.reconnect()
        print("Move action:")
        controlNum = int(controlNum)
        print(controlNum)

        if(controlNum == 0):
            self.servo0_pos = self.servo0_pos + self.movedeg
            if((self.servo0_pos <= self.servo0_hi_lim) and (self.servo0_pos >= self.servo0_lo_lim)):
                self.kit.servo[0].angle = int(self.servo0_pos)           
            elif(self.servo0_pos > self.servo0_hi_lim):
                self.servo0_pos = int(self.servo0_hi_lim)
                self.kit.servo[0].angle = int(self.servo0_pos)
            elif(self.servo0_pos < self.servo0_lo_lim):
                self.servo0_pos = int(self.servo0_lo_lim)
                self.kit.servo[0].angle = int(self.servo0_pos)
        elif(controlNum == 1):
            self.servo0_pos = self.servo0_pos - self.movedeg
            if((self.servo0_pos <= self.servo0_hi_lim) and (self.servo0_pos >= self.servo0_lo_lim)):
                print("move s0")
                self.kit.servo[0].angle = int(self.servo0_pos)
            elif(self.servo0_pos > self.servo0_hi_lim):
                self.servo0_pos = int(self.servo0_hi_lim)
                self.kit.servo[0].angle = int(self.servo0_pos)
            elif(self.servo0_pos < self.servo0_lo_lim):
                self.servo0_pos = int(self.servo0_lo_lim)
                self.kit.servo[0].angle = int(self.servo0_pos)
        elif(controlNum == 2):
            self.servo1_pos = self.servo1_pos + self.movedeg
            if(self.servo1_pos <= self.servo1_hi_lim) and (self.servo1_pos >= self.servo1_lo_lim):
                print("move s1")
                self.kit.servo[1].angle = int(self.servo1_pos)
            elif(self.servo1_pos > self.servo1_hi_lim):
                self.servo1_pos = int(self.servo1_hi_lim)
                self.kit.servo[1].angle = int(self.servo1_pos)
            elif(self.servo1_pos < self.servo1_lo_lim):
                self.servo1_pos = int(self.servo1_lo_lim)
                self.kit.servo[1].angle = int(self.servo1_pos)
        elif(controlNum == 3):
            self.servo1_pos = self.servo1_pos - self.movedeg
            if(self.servo1_pos <= self.servo1_hi_lim) and (self.servo1_pos >= self.servo1_lo_lim):
                print("move s1")
                self.kit.servo[1].angle = int(self.servo1_pos)
            elif(self.servo1_pos > self.servo1_hi_lim):
                self.servo1_pos = int(self.servo1_hi_lim)
                self.kit.servo[1].angle = int(self.servo1_pos)
            elif(self.servo1_pos < self.servo1_lo_lim):
                self.servo1_pos = int(self.servo1_lo_lim)
                self.kit.servo[1].angle = int(self.servo1_pos)
        elif(controlNum == 4):
            self.servo2_pos = self.servo2_pos + self.movedeg
            if(self.servo2_pos <= self.servo2_hi_lim) and (self.servo2_pos >= self.servo2_lo_lim):    
                print("move s2")
                self.kit.servo[2].angle = int(self.servo2_pos)
            elif(self.servo2_pos > self.servo2_hi_lim):
                self.servo2_pos = int(self.servo2_hi_lim)
                self.kit.servo[2].angle = int(self.servo2_pos)
            elif(self.servo2_pos < self.servo2_lo_lim):
                self.servo2_pos = int(self.servo2_lo_lim)
                self.kit.servo[2].angle = int(self.servo2_pos)
        elif(controlNum == 5):
            self.servo2_pos = self.servo2_pos - self.movedeg
            if(self.servo2_pos <= self.servo2_hi_lim) and (self.servo2_pos >= self.servo2_lo_lim):    
                print("move s2")
                self.kit.servo[2].angle = int(self.servo2_pos)
            elif(self.servo2_pos > self.servo2_hi_lim):
                self.servo2_pos = int(self.servo2_hi_lim)
                self.kit.servo[2].angle = int(self.servo2_pos)
            elif(self.servo2_pos < self.servo2_lo_lim):
                self.servo2_pos = int(self.servo2_lo_lim)
                self.kit.servo[2].angle = int(self.servo2_pos)
        elif(controlNum == 6):
            self.servo3_pos = self.servo3_pos + self.movedeg
            if(self.servo3_pos <= self.servo3_hi_lim) and (self.servo3_pos >= self.servo3_lo_lim):    
                print("move s3")
                self.kit.servo[3].angle = int(self.servo3_pos)
            elif(self.servo3_pos > self.servo3_hi_lim):
                self.servo3_pos = int(self.servo3_hi_lim)
                self.kit.servo[3].angle = int(self.servo3_pos)
            elif(self.servo3_pos < self.servo3_lo_lim):
                self.servo3_pos = int(self.servo3_lo_lim)
                self.kit.servo[3].angle = int(self.servo3_pos)
        elif(controlNum == 7):
            self.servo3_pos = self.servo3_pos - self.movedeg
            if(self.servo3_pos <= self.servo3_hi_lim) and (self.servo3_pos >= self.servo3_lo_lim):    
                print("move s3")
                self.kit.servo[3].angle = int(self.servo3_pos)
            elif(self.servo3_pos > self.servo3_hi_lim):
                self.servo3_pos = int(self.servo3_hi_lim)
                self.kit.servo[3].angle = int(self.servo3_pos)
            elif(self.servo3_pos < self.servo3_lo_lim):
                self.servo3_pos = int(self.servo3_lo_lim)
                self.kit.servo[3].angle = int(self.servo3_pos)
        elif(controlNum == 8):
            self.servo4_pos = self.servo4_pos + self.movedeg
            if(self.servo4_pos <= self.servo4_hi_lim) and (self.servo4_pos >= self.servo4_lo_lim):    
                self.kit.servo[4].angle = int(self.servo4_pos)
                print("move s4")
            elif(self.servo4_pos > self.servo4_hi_lim):
                self.servo4_pos = int(self.servo4_hi_lim)
                self.kit.servo[4].angle = int(self.servo4_pos)
            elif(self.servo4_pos < self.servo4_lo_lim):
                self.servo4_pos = int(self.servo4_lo_lim)
                self.kit.servo[4].angle = int(self.servo4_pos)
        elif(controlNum == 9):
            self.servo4_pos = self.servo4_pos - self.movedeg
            if(self.servo4_pos <= self.servo4_hi_lim) and (self.servo4_pos >= self.servo4_lo_lim):    
                self.kit.servo[4].angle = int(self.servo4_pos)
                print("move s4")
            elif(self.servo4_pos > self.servo4_hi_lim):
                self.servo4_pos = int(self.servo4_hi_lim)
                self.kit.servo[4].angle = int(self.servo4_pos)
            elif(self.servo4_pos < self.servo4_lo_lim):
                self.servo4_pos = int(self.servo4_lo_lim)
                self.kit.servo[4].angle = int(self.servo4_pos)
        elif(controlNum == 10):
            self.servo5_pos = self.servo5_pos + self.movedeg
            if(self.servo5_pos <= self.servo5_hi_lim) and (self.servo5_pos >= self.servo5_lo_lim):    
                print("move s5")
                self.kit.servo[5].angle = int(self.servo5_pos)
            elif(self.servo5_pos > self.servo5_hi_lim):
                self.servo5_pos = int(self.servo5_hi_lim)
                self.kit.servo[5].angle = int(self.servo5_pos)
            elif(self.servo5_pos < self.servo5_lo_lim):
                self.servo5_pos = int(self.servo5_lo_lim)
                self.kit.servo[5].angle = int(self.servo5_pos)
        elif(controlNum == 11):
            self.servo5_pos = self.servo5_pos - self.movedeg
            if(self.servo5_pos <= self.servo5_hi_lim) and (self.servo5_pos >= self.servo5_lo_lim):    
                print("move s5")
                self.kit.servo[5].angle = int(self.servo5_pos)
            elif(self.servo5_pos > self.servo5_hi_lim):
                self.servo5_pos = int(self.servo5_hi_lim)
                self.kit.servo[5].angle = int(self.servo5_pos)
            elif(self.servo5_pos < self.servo5_lo_lim):
                self.servo5_pos = int(self.servo5_lo_lim)
                self.kit.servo[5].angle = int(self.servo5_pos)



        #movement time
        start = time.time()
        stop = False
        while(not(stop)):
            now = time.time()
            if(now - start > 1):
                stop = True
        self.print_info()




    def move_servo(self,svn,pos):
        self.kit.servo[svn].angle = int(pos)

    def print_info(self):
        print("Servo 0: " + str(self.servo0_pos))
        print("Servo 1: " + str(self.servo1_pos))
        print("Servo 2: " + str(self.servo2_pos))
        print("Servo 3: " + str(self.servo3_pos))
        print("Servo 4: " + str(self.servo4_pos))
        print("Servo 5: " + str(self.servo5_pos))
