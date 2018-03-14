import  cv2 as cv
src=cv.imread("E:/opencv_pictures/test.jpg")
cv.namedWindow("test",cv.WINDOW_AUTOSIZE)
cv.imshow("test",src)
cv.waitKey(0)
cv.destroyAllWindows()


