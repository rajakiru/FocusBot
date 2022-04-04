from playsound import playsound

voicefpath = "/Users/kiruthika/Shibaura/BioDataRecorder_MindwaveOnly_ver20210528/For DePauwVer0528/Alert System/Voice/"
intro = voicefpath + 'Introduction.mp3'
intro = intro.replace(" ", "%20")
playsound(intro)

better = "/Users/kiruthika/Shibaura/BioDataRecorder_MindwaveOnly_ver20210528/For DePauwVer0528/Alert System/Voice/Better.mp3"
better = better.replace(" ", "%20")
playsound(better)

concdrop2 = "/Users/kiruthika/Shibaura/BioDataRecorder_MindwaveOnly_ver20210528/For DePauwVer0528/Alert System/Voice/ConcDropping2.mp3"
concdrop2 = concdrop2.replace(" ", "%20")
playsound(concdrop2)
