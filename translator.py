from deep_translator import GoogleTranslator
import threading

def translate_1(first,second,text):
    translated = GoogleTranslator(source=first, target=second).translate(text)
    return translated
def translate(first,second,text):
    t = threading.Thread(target = translate_1,args=[first,second,text])
    t.start()
    t.join()

