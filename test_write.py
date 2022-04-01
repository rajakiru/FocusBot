import time
import pandas as pd
import cv2

fpath = "faceDB/"
normal = 1

try:
    while True:
        # Read data from file 'filename.csv'
        df = pd.read_csv("/Users/kiruthika/Shibaura/BioDataRecorder_MindwaveOnly_ver20210528/For DePauwVer0528/MindstreamPy-main/sample0528.csv", usecols = ['attention','meditation'])
        time.sleep(1)
        lastdata = (df.tail(1))
        # read attention from row
        for index, row in lastdata.iterrows():
            attention = row['attention']
        print (attention)
        df.to_csv('test.csv')

        if normal == 8:
            normal = 1
        image = cv2.imread(fpath + 'normal' + str(normal) + '.jpg', 0)
        cv2.imshow('Robot Alert System', image)
        cv2.waitKey(1000)
        normal +=1

except KeyboardInterrupt:
    print('ctrl + c')
