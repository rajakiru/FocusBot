import time
import pandas as pd
from playsound import playsound

lowdf = 0
highdf = 0
contdropdf = 0
betterdf = 0

voicefpath = "/Users/kiruthika/Shibaura/BioDataRecorder_MindwaveOnly_ver20210528/For DePauwVer0528/Alert System/Voice/"
intro = voicefpath + 'Introduction.mp3'
intro = intro.replace(" ", "%20")
good = voicefpath + 'DoingGreat.mp3'
good = good.replace(" ", "%20")
lowconc = voicefpath + 'ConDropping1.mp3'
lowconc = lowconc.replace(" ", "%20")
concdropping = voicefpath + 'ConcDropping2.mp3'
concdropping = concdropping.replace(" ", "%20")
better = voicefpath + 'Better.mp3'
better = better.replace(" ", "%20")
end = voicefpath + 'End.mp3'
end = end.replace(" ", "%20")
# Only Two Conditions

playsound(intro)
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
        if attention < 40:
            contdropdf+=1
            lowdf += 1
            betterdf=0
            highdf=0
            if lowdf > 5 and contdropdf < 10:
                playsound(lowconc)
                print('Attention is low')
                lowdf = 0
            elif contdropdf == 15:
                playsound(concdropping)
                print('Attention is Continuously Dropping')
                lowdf=0
                contdropdf=0
            else:
                continue
        else:
            if contdropdf == 6:
                betterdf+=1
                if betterdf > 20:
                    playsound(better)
                    print('Attention is increasing, better')
                    betterdf = 0
                    contdropdf = 0
            elif contdropdf != 6:
                highdf += 1
                lowdf = 0
                contdropdf = 0
                if highdf > 30:
                    playsound(good)
                    print('Attention is high')
                    highdf = 0
            else:
                continue

except KeyboardInterrupt:
    print('ctrl + c')

playsound(end)
