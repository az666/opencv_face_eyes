import  cv2 as cv
import numpy as  np


def face_detect_demo (image):
    # 图形空间转换为灰度图
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # 加载人脸数据
    # facea_shuju = "E:/HelloWord/opencv/opencv-master/data/haarcascades/haarcascade_frontalface_alt_tree.xml"
    lbp_face_shuju = "E:/HelloWord/opencv/opencv-master/data/lbpcascades/lbpcascade_frontalface_improved.xml"
    # 检测人眼数据
    eyes = "E:/HelloWord/opencv/opencv-master/data/haarcascades/haarcascade_eye.xml"
    eyes_detector = cv.CascadeClassifier(eyes)
    face_detector = cv.CascadeClassifier(lbp_face_shuju)
    faces = face_detector.detectMultiScale(gray,1.3,3)#1.3和5是特征的最小、最大检测窗口，它改变检测结果也会改变
   # eyess = eyes_detector.detectMultiScale(gray,1,3,2)
    print(faces)
   # for x,y,w,h in eyess:
        # 标出眼部图像
    #    cv.rectangle(image,(x,y),(x+w,y+w),(0,0,255),2)
    for x,y,w,h in faces:
        # 标出脸部图像
        cv.rectangle(image,(x,y),(x+w,y+w),(0,0,255),2)
    cv.imshow("face",image)
    cv.waitKey(10)
capture = cv.VideoCapture(0)
cv.namedWindow("face",cv.WINDOW_AUTOSIZE)
while (True):
    ret,frame = capture.read()
    frame = cv.flip(frame,1)
    face_detect_demo(frame)
    c = cv.waitKey(10)
    if c == 27: # 代表esc按键
        break



src=cv.imread("E:/opencv_pictures/lena.jpg")
#cv.namedWindow("test",cv.WINDOW_AUTOSIZE)

#cv.imshow("test",src)
cv.waitKey(0)
cv.destroyAllWindows()