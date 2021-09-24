from gtts import gTTS
import os

file = open("adi.txt",'r').read()
language = 'hi'
output = gTTS(text=file,lang=language,slow=False)
output.save('adu.mp3')

os.system("start adu.mp3")