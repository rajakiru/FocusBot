import time
import pandas as pd
import cv2

fpath = "faceDB/"
lowdf= 0
highdf = 0
contdropdf = 0
betterdf = 0
normal = 1

try:
    while True:
        df = pd.read_csv("/Users/kiruthika/Shibaura/BioDataRecorder_MindwaveOnly_ver20210528/For DePauwVer0528/MindstreamPy-main/sample0528.csv", usecols = ['attention','meditation'])
        time.sleep(1)
        lastdata = (df.tail(1))

        for index, row in lastdata.iterrows():
            attention = row['attention']
        print(attention)

        if normal == 8:
            normal = 1
        image = cv2.imread(fpath + 'normal' + str(normal) + '.jpg', 0)
        cv2.imshow('Robot Alert System', image)
        cv2.waitKey(1000)
        normal +=1

if attention < 40:
    contdropdf+=1
    lowdf += 1
    betterdf=0
    highdf=0
    if lowdf > 5 and contdropdf < 10:
        i = 1 #Conc Drop Alert Facial Expressions
        for i in range(1,4):
            image = cv2.imread(fpath + 'serious' + str(i) + '.jpg', 0)
            cv2.imshow('Robot Alert System', image)
            cv2.waitKey(1000)
            i+=1
        lowdf = 0
        print('Attention is Dropping')

    elif contdropdf > 15:
        i = 1  # Conc Continuously Drop Facial Expressions
        for i in range(1,4):
            image = cv2.imread(fpath + 'serious' + str(i) + '.jpg', 0)
            cv2.imshow('Robot Alert System', image)
            cv2.waitKey(3000)
            i+=1
        lowdf=0
        print('Attention is Continuously Dropping')
    else:
        continue
else:
    if contdropdf == range(10,20):
        betterdf+=1
        if betterdf > 10:
            i = 1 #Happy/ High Conc Alert Facial Expressions
            for i in range(1,4):
                image = cv2.imread(fpath + 'happy' + str(i) + '.jpg', 0)
                cv2.imshow('Robot Alert System', image)
                cv2.waitKey(2000)
                i+=1
            print('Attention is better')
            betterdf = 0
            contdropdf = 0

    elif contdropdf != range(10,20):
        highdf += 1
        lowdf = 0
        contdropdf = 0
        if highdf > 20:
            i = 1 #Happy/ High Conc Alert Facial Expressions
            for i in range(1,4):
                image = cv2.imread(fpath + 'happy' + str(i) + '.jpg', 0)
                cv2.imshow('Robot Alert System', image)
                cv2.waitKey(2000)
                i+=1
            print('Attention is Good')
            highdf = 0
    else:
        continue

except KeyboardInterrupt:
print('ctrl + c')
