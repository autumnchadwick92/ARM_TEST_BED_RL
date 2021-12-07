import cv2
import imutils
from imutils import perspective
from imutils import contours
import numpy as np
from scipy import ndimage
import math
from matplotlib import pyplot as plt



class reward():

    def __init__(self):
        #usb webcams
        self.cam1 = cv2.VideoCapture("/dev/video0")
        self.cam2 = cv2.VideoCapture("/dev/video1")
        self.cam1.set(3,64)
        self.cam1.set(4,64)
        self.cam2.set(3,64)
        self.cam2.set(4,64)


        self.reward_val = 0
        self.move_penalty = -0.75

        #determined by image size 
        self.max_dist =  500
        #final destination goal size
        self.final_dest = 5


    def reward_cal(self):
        self.reward_val = self.reward_val + self.move_penalty + (1-(self.calc_dist()/self.max_dist))
        print(self.reward_val)
        return self.reward_val



    def get_state(self):
        
        while(True):
            ret1,image1 = self.cam1.read()
            
            if(ret1 == True):
                break
        
            self.cam1 = cv2.VideoCapture("/dev/video0")
            self.cam2 = cv2.VideoCapture("/dev/video1")
            self.cam1.set(3,64)
            self.cam1.set(4,64)
            self.cam2.set(3,64)
            self.cam2.set(4,64)



        image1 = cv2.resize(image1,(32,32),interpolation=cv2.INTER_AREA)
        return image1

        


    def calc_dist(self):
        ret1 = False
        ret2 = False

        #take capture
        while(not(ret1 and ret2)):
            ret1,image1 = self.cam1.read()
            ret2,image2 = self.cam2.read()
            
        image1 = cv2.flip(image1, 1 )
        image2 = cv2.flip(image2, 1 )

        
 
        hsv1 = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
        hsv2 = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)


        # define yellow color range
        #(0-179, 0-255,0-255)
        light_green = np.array([30,44,43])
        dark_green = np.array([70,254,254])

        #define pink color range
        #light_pink = np.array([135,48,43])
        #dark_pink = np.array([175,254,254])

        #define yellow
        light_yellow = np.array([25,143,174])
        dark_yellow = np.array([144,189,205])


        # Threshold the HSV image to get only yellow colors
        mask_1_1 = cv2.inRange(hsv1, light_green, dark_green)
        mask_1_2 = cv2.inRange(hsv1, light_yellow, dark_yellow)

        mask_2_1 = cv2.inRange(hsv2, light_green, dark_green)
        mask_2_2 = cv2.inRange(hsv2, light_yellow, dark_yellow)

        self.cam1.release()
        self.cam2.release()

        #find center of mass of mask
        cm1 = ndimage.center_of_mass(mask_1_1)
        cm2 = ndimage.center_of_mass(mask_1_2)
        cm3 = ndimage.center_of_mass(mask_2_1)
        cm4 = ndimage.center_of_mass(mask_2_2)

        print(cm1)
        print(cm2)
        print(cm3)
        print(cm4)

        cm1 = list(cm1)
        cm2 = list(cm2)
        cm3 = list(cm3)
        cm4 = list(cm4)


        if(np.isnan(cm1[0])):
            cm1[0] = 99 

        if(np.isnan(cm1[1])):
            cm1[1] = 99 

        if(np.isnan(cm2[0])):
            cm2[0] = 99 

        if(np.isnan(cm2[1])):
            cm2[1] = 99 

        if(np.isnan(cm3[0])):
            cm3[0] = 99 

        if(np.isnan(cm3[1])):
            cm3[1] = 99 

        if(np.isnan(cm4[0])):
            cm4[0] = 99 

        if(np.isnan(cm4[1])):
            cm4[1] = 99 


        #convert to int
        x1 = int(cm1[1])
        y1 = int(cm1[0])

        x2 = int(cm2[1])
        y2 = int(cm2[0])


        x3 = int(cm3[1])
        y3 = int(cm3[0])

        x4 = int(cm4[1])
        y4 = int(cm4[0])


        d1 = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        d2 = math.sqrt((x3-x4)**2 + (y3-y4)**2)

        #print(d1)
        #print(d2)

        dist = d1+d2

        print(dist)

        if(dist < self.final_dest):
            dist = 0

        return dist

