import cv2 as cv
import numpy as np
def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret,frame = capture.read()
        frame = cv.flip(frame,1)
        cv.imshow ("video",frame)
        c = cv.waitKey (50)
        if c == 27:  # 相当于人为退出
            break


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)


print("加载图像测试")
src = cv.imread("E:/opencv_pictures/test.jpg")
# cv.namedWindow("test",cv.WINDOW_AUTOSIZE)
# cv.imshow("test",src)
get_image_info(src)
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imwrite("E:/opencv_pictures/test_output.jpg",gray)
video_demo()
cv.waitKey(0)
cv.destroyAllWindows()