import cv2
import numpy as np

kernel = np.ones((2,5),np.uint8)
print(kernel)

path = "D:/computer vision/1.jpg"
img =  cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Lena",img)
cv2.imshow("GrayScale",imgGray)
cv2.waitKey(0)
