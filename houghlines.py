# coding=utf-8
# 霍夫直线算法
import  cv2 as cv
import numpy as np
def line_detection(image):
    # 颜色空间转换
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray,50,150,apertureSize=3)
    lines = cv.HoughLines(edges,1,np.pi/180,200)
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0+1000*(-b))
        y1 = int(y0+1000*(a))
        x2 = int(x0-1000*(-b))
        y2 = int(y0-1000*(a))
        cv.line(image,(x1,y1),(x2,y2),(0,0,255),2)
        cv.imshow("huofu",image)

src=cv.imread("E:/opencv_pictures/test.jpg")
src2=cv.imread("E:/opencv_pictures/sudoku.png")
cv.namedWindow("test",cv.WINDOW_AUTOSIZE)
cv.imshow("test",src2)
line_detection(src2)
cv.waitKey(0)
cv.destroyAllWindows()