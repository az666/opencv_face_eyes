# coding=utf-8
import  cv2 as cv


def edge_demo(image):
    # 高斯模糊，降噪
    blurred = cv.GaussianBlur(image,(3,3),0)
    # 颜色空间转换
    gray = cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    # 边缘算子
    xgrad = cv.Sobel(gray,cv.CV_16SC1,1,0)
    ygrad = cv.Sobel(gray,cv.CV_16SC1,0,1)
    # 边缘捕捉canny
    edge_output= cv.Canny(xgrad,ygrad,50,150)
    cv.imshow("canny",edge_output)
    # 与操作,实现彩色
    #dst = cv.bitwise_and(image,image,mask=edge_output)
    #cv.imshow("canny_color",dst)

def camera() :
    capture = cv.VideoCapture(0)
    while (True):
        ret, frame = capture.read()
        if ret == False:
            break
        edge_demo(frame)
        c = cv.waitKey(50)
        if c == 27:  # 相当于人为退出
            break


src=cv.imread("E:/opencv_pictures/test.jpg")
cv.namedWindow("test",cv.WINDOW_AUTOSIZE)
cv.imshow("test",src)
#edge_demo(src)
camera()
cv.waitKey(0)
cv.destroyAllWindows()