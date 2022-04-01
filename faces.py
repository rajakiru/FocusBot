import time
import pandas as pd
import cv2

fpath = "faceDB/"
lowdf = 0
highdf = 0

i = 1
for i in range(1,4):
    image = cv2.imread(fpath + 'happy' + str(i) + '.jpg', 0)
    cv2.imshow('Robot Alert System', image)
    cv2.waitKey(2000)
    i+=1

i = 1
for i in range(1,4):
    image = cv2.imread(fpath + 'neutral' + str(i) + '.jpg', 0)
    cv2.imshow('Robot Alert System', image)
    cv2.waitKey(2000)
    i+=1
