import cv2 as cv
import numpy as np


def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        #  打开摄像头
        ret,frame = capture.read()
        if ret == False:
            break
        #  转换为hsv图像
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        #  下阈值
        lower_hsv = np.array([37,43,46])
        #  上阈值
        upper_hsv = np.array([77,255,255])
        mask = cv.inRange(hsv,lowerb=lower_hsv,upperb = upper_hsv)
        #  cv.inRange(目标图像，阈值下，阈值上，输出图像)
        cv.imshow ("video",frame)
        cv.imshow ( "mask",mask)
        c = cv.waitKey (50)
        if c == 27:  # 相当于人为退出
            break


video_demo()
