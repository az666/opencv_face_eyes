# coding=utf-8
import cv2 as cv
import  numpy as np
def detect_circle_demo (image):
    #  降噪处理
    dst = cv.pyrMeanShiftFiltering(image,10,25)
    cv.imshow("jiangzao",dst)
    cimage = cv.cvtColor(dst,cv.COLOR_BGR2GRAY)  #  灰度图转换
    print("正在灰度转换。。。。。。")
    cv.imshow("test",cimage)
    #  霍夫圆处理
    circles = cv.HoughCircles(cimage,cv.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
    print("原值",circles)
    #  转换为整数
    circles = np.uint16(np.around(circles))
    print("转换为整数",circles)
    for i in circles[0,:]:
        cv.circle(image,(i[0],i[1]),i[2],(0,0,255),2)
        cv.circle(image,(i[0],i[1]),2,(255,0,0),2)
    cv.imshow("circle",image)

src = cv.imread("E:/opencv_pictures/stuff.jpg")
cv.namedWindow("output",cv.WINDOW_AUTOSIZE)
cv.imshow("output",src)
detect_circle_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()

