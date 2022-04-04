import time
import pandas as pd

df = pd.read_csv("/Users/kiruthika/Shibaura/BioDataRecorder_MindwaveOnly_ver20210528/For DePauwVer0528/MindstreamPy-main/sample0528.csv")

# # Read headers
# print(df.columns)
#Read Each column
# print(df[['attention', 'meditation']][40:45])

# #Read Each Row
# print(df.iloc[0:4])
# for index, row in lastdata.iterrows():
#     print(index, row['attention'])

# #Read specific location
# print(df.iloc[2,4])

# # Read last few data using tail and first using head
# lastdata= df.tail(2)
lastdata = df.iloc[40:41]
print(lastdata[['attention', 'meditation']])

# if df.empty:
#     print('DataFrame is empty!')


for index, row in lastdata.iterrows():
    attention = row['attention']
    if attention >= 40:
        print('Attention is high')
