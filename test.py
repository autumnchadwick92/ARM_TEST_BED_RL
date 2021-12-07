from action import action
import cv2
import time

#from reward import reward
#rw = reward()
#rw.calc_dist()

a = action()
cap = cv2.VideoCapture('/dev/video0')

def nothing(x):
    pass


cv2.namedWindow("Trackbars")
cv2.createTrackbar("0- L - H", "Trackbars", 30, 270, nothing)
cv2.createTrackbar("1- L - H", "Trackbars", 20, 180, nothing)
cv2.createTrackbar("2- L - H", "Trackbars", 20, 340, nothing)
cv2.createTrackbar("3- L - H", "Trackbars", 220, 359, nothing)
cv2.createTrackbar("4- L - H", "Trackbars", 0, 180, nothing)
cv2.createTrackbar("5- L - H", "Trackbars", 0, 180, nothing)


while(True):
    ret, frame = cap.read()

    l_h0 = cv2.getTrackbarPos("0- L - H", "Trackbars")
    l_h1 = cv2.getTrackbarPos("1- L - H", "Trackbars")
    l_h2 = cv2.getTrackbarPos("2- L - H", "Trackbars")
    l_h3 = cv2.getTrackbarPos("3- L - H", "Trackbars")
    l_h4 = cv2.getTrackbarPos("4- L - H", "Trackbars")
    l_h5 = cv2.getTrackbarPos("5- L - H", "Trackbars")

    cv2.imshow('Trackbars',frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

    a.move_servo(1,l_h1)
    a.move_servo(2,l_h2)
    a.move_servo(3,l_h3)
    a.move_servo(4,l_h4)
    a.move_servo(5,l_h5)
    a.move_servo(0,l_h0)


    



