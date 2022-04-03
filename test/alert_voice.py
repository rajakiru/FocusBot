import time
import pandas as pd
from playsound import playsound

better = "/Users/kiruthika/Shibaura/BioDataRecorder_MindwaveOnly_ver20210528/For DePauwVer0528/Alert System/Voice/Better.mp3"
better = better.replace(" ", "%20")

df = pd.read_csv("/Users/kiruthika/Shibaura/BioDataRecorder_MindwaveOnly_ver20210528/For DePauwVer0528/MindstreamPy-main/sample0528.csv")
lastdata = df.iloc[40:45]

for index, row in lastdata.iterrows():
    attention = row['attention']
    if attention >= 40:
        playsound(better)
