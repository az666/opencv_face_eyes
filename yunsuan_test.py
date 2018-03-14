import  cv2 as cv

def add_demo(m1,m2):   # 加法操作
    dst = cv.add(m1,m2)
    cv.imshow("add_demo",dst)
def subtract_demo(m1,m2): # 减法操作
    dst = cv.subtract(m1,m2)
    cv.imshow("subtract_demo",dst)
def multiply_demo(m1,m2): # 乘法操作
    dst = cv.multiply(m1,m2)
    cv.imshow("multiply",dst)

def divide_demo(m1,m2):  # 除法操作
    dst = cv.divide(m1,m2)
    cv.imshow("divide_demo",dst)


src1 = cv.imread("E:/opencv_pictures/LinuxLogo.jpg")
src2 = cv.imread("E:/opencv_pictures/WindowsLogo.jpg")
print(src1.shape)
print(src2.shape)
# cv.namedWindow("linux",cv.WINDOW_AUTOSIZE)
cv.imshow("linux",src1)
cv.imshow("windows",src2)
add_demo(src1,src2)
subtract_demo(src1,src2)
cv.waitKey(0)
cv.destroyAllWindows()