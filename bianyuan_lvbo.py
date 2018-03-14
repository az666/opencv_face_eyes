# coding=utf-8
import cv2 as cv
import numpy as np
def bi_demo (image):
    print ("ceshi")
    dst = cv.bilateralFilter(image,0,100,15)
    cv.imshow("bi_demo",dst)
def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image,10,50)
    cv.imshow("shift_demo",dst)
src =cv.imread("E:/opencv_pictures/face.jpg")
#  压缩图片
src = cv.resize(src, (300, 200), interpolation=cv.INTER_AREA)
cv.namedWindow("test",cv.WINDOW_AUTOSIZE)
cv.imshow("test",src)
bi_demo(src)
shift_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()