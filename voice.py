import pyttsx3
import threading

def text_to_voice_run(text):
    sound = pyttsx3.init()
    sound.setProperty('rate',100)
    sound.say(text)
    sound.runAndWait()

def text_to_voice(text):
    t = threading.Thread(target = text_to_voice_run,args = [text])
    t.start()
