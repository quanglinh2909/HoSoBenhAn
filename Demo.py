import math

from ultralytics import YOLO
import cv2
import numpy as np

image = cv2.imread("z4551472697649_cdff37cdbb2672eea0a06c972b823ed0.jpg")


(h, w) = image.shape[:2]
center = (w / 2, h / 2)
M = cv2.getRotationMatrix2D(center, 20, 1.0)
image = cv2.warpAffine(image, M, (w, h))

#save image
cv2.imwrite("test.jpg", image)

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
