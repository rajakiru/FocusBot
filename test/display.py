import time
import pandas as pd
import cv2

#Facial Expressions - read images
normal1 = cv2.imread('faceDB/relax2.JPG', 0)
normal2 = cv2.imread('faceDB/happy1.jpg', 0)
normal3 = cv2.imread('faceDB/happy2.jpg', 0)
normal4 = cv2.imread('faceDB/happy3.jpg', 0)
normal5 = cv2.imread('faceDB/relax3.JPG', 0)
normal6 = cv2.imread('faceDB/relax4.JPG', 0)
normal7 = cv2.imread('faceDB/relax5.JPG', 0)

happy1 = cv2.imread('faceDB/happy3.JPG', 0)
happy2 = cv2.imread('faceDB/happy4.jpg', 0)
happy3 = cv2.imread('faceDB/happy5.jpg', 0)

serious1 = cv2.imread('faceDB/neutral.JPG', 0)
serious2 = cv2.imread('faceDB/anger1.JPG', 0)
serious2 = cv2.imread('faceDB/anger2.JPG', 0)

neutral1 = cv2.imread('faceDB/neutral.JPG', 0)
neutral2 = cv2.imread('faceDB/relax1.JPG', 0)

# test display

cv2.imshow('Robot Alert System', normal1)
cv2.waitKey(3000)
cv2.imshow('Robot Alert System', normal2)
cv2.waitKey(3000)
if k == 13: cv2.destroyAllWindows()
else      : pass


# more extra

# read the image
img = cv2.imread('faceDB/happy1.JPG', 0)

#test cv2 by saving a file
#cv2.imwrite('face_test.JPG',img)

# display image by creating window Face
while(1):
     cv2.imshow('Robot Alert System', img)
     k = cv2.waitKey(33)
     if k==27:
         break
     elif k==-1:
        continue

# To close the window after the required kill value was provided
cv2.destroyAllWindows()

#show images
from PIL import Image
img = Image.open('faceDB/happy1.JPG')
img.show()
