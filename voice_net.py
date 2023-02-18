import playsound
from  gtts import gTTS
from langs import conv
import threading
import os

def speak_2(text,langu):
    try : 
        os.remove('voice.mp3')
    except :
        pass
    voice = gTTS(text=text , lang=conv(langu))
    filename = 'voice.mp3'
    voice.save(filename)
    playsound.playsound(filename)

def speak(text,langu):
    t = threading.Thread(target = speak_2,args=[text,langu])
    t.start()

