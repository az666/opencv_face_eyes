# coding=utf-8
import cv2
import numpy as np
# 寻找人的位置
def self_detect(img):
    # 传入RIO区域
    region_upper = int(img.shape[0]*0.3)
    region_lower = int(img.shape[0]*0.7)
    # 切片操作
    region = img[region_upper:region_lower]
    # 获得hsv图像
    hsv_img = cv2.cvtColor(region,cv2.COLOR_BGR2HSV)
    color_lower = np.int32([105,25,45])
    color_upper = np.int32([135,125,130])
    color_mask = cv2.inRange(hsv_img,color_lower,color_upper)
    # 寻找轮廓最大点，并返回
    contours = cv2.findContours(color_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[1]
    if len(contours)>0:
        max_contour = max(contours,key = cv2.contourArea)
        max_contour = cv2.convexHull(max_contour)
        rect = cv2.boundingRect(max_contour)
        x,y,w,h = rect
        center_coord = (x+int(w/2),y+h+region_upper - 20)
        #  在目标区域画一个圆 参数为（图像，圆心，半径，颜色）
        cv2.circle(img,center_coord,5,(0,255,0),-1)
        return center_coord
    #cv2.imshow("test",color_mask)

# 寻找下一个箱子的位置
def goal_detcet(img,body_position):
    region_upper = int(img.shape[0] * 0.3)
    region_lower = int(img.shape[0] * 0.7)
    if body_position[0]<(img.shape[1]/2.0):
        region_left = body_position[0]+30
        region_right = img.shape[1]-30
    else:
        region_left=30
        region_right = body_position[0]-30
        # 切片操作
    region = img[region_upper:region_lower,region_left:region_right]
    cv2.imshow("test",region)




img = cv2.imread("E:/opencv_pictures/jump2.png")
img = cv2.resize(img,(720,1080))
pos= self_detect(img)
goal_detcet(img,pos)
cv2.waitKey(0)



