import cv2
import numpy as np
img = cv2.imread('"D:\computer vision\1.jpg"' cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
cv2.imshow('Input Image', img)
cv2.imshow('Erosion', erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
