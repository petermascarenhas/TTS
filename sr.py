import speech_recognition as sr
from gtts import gTTS



def s2t():
    myVoice=""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio= r.listen(source)

        myVoice= r.recognize_google(audio)
        print myVoice
        tts = gTTS(text=myVoice, lang ="en")
        tts.save('hello.mp3')
    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     audio= r.listen(source)
    #
    #     print r.recognize_google(audio)

s2t()