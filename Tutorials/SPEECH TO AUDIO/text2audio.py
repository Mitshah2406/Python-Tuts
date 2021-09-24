from gtts import gTTS   #module for converting into audio
import os   #module for opening a media player

name = "Aditya Shah"  
output= gTTS(text=name,lang="en",slow=False)#here, gTTS is used text is attribute which takes text as input lang is specifying language and slow is set to false because we want it to say fast
output.save('ou.mp3')  #in this the audio getting saved

os.system("start ou.mp3")# in this we are saying to system to play the mp3 file.