import cv2

import numpy as np

kernel = np.ones((5,5),np.uint8)

print(kernel)

path = "D:/computer vision/1.jpg"

img =  cv2.imread(path)

imgDilation = cv2.dilate(img,kernel , iterations = 10)

cv2.imshow("Img Dialation",imgDilation)

cv2.waitKey(0)
