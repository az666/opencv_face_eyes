import  cv2 as cv
import  numpy as np
# 获取图像的像素点 但是耗时较长
def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width : %s, height : %s channels : %s"%(width,height,channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row,col,c]
                image[row,col,c]=255 - pv
    cv.imshow("pixels",image)

# 同样获取像素，但速度极快，调用的api
def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("inverse test",dst)


def create_image():
    # 新建一个3通道的图像
    # 通道为 blue green red 对应0 1 2

    img = np.zeros([400,400,3],np.uint8)
    img[:,:,0] = np.ones([400,400])*255
    cv.imshow("new image", img)


src=cv.imread("E:/opencv_pictures/test.jpg")
cv.namedWindow("test",cv.WINDOW_AUTOSIZE)
t1 = cv.getTickCount()     # cpu 到现在的运行时间

cv.imshow("test",src)
# access_pixels(src)
inverse(src)
# create_image()
t2 = cv.getTickCount()  # CPU 到现在的运行时间
time = (t2-t1)/cv.getTickFrequency()
print("time :%s ms"%(time*1000))    # 输出加载时间
cv.waitKey(0)
cv.destroyAllWindows()