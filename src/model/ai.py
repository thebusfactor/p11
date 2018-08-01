import cv2 as cv
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt
import numpy

from util.classification import Classification

options = {"model": "cfg/yolo.cfg", "load": "bin/yolov2.weights", "threshold": 0.1}

tfnet = TFNet(options)


img = cv.imread("bin/Bus1.jpg")
img = cv.resize(img, (1920, 1080))

results = tfnet.return_predict(img)
# cv.imshow("result", img)
# print(result)

for res in results:
    clf = Classification(res)
    print(clf)




cv.waitKey(0)