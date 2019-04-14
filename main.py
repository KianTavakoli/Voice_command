import speech_recognition as sr
import Google
import YouTube
import Voice
import Activation
# initialize speech recognizer and mic
mic = sr.Microphone()
rec = sr.Recognizer()
en = Voice

while True:
    if Activation.Activation.activate:
        en.Voice.en("Hello Kian")
        while True:
            # noinspection PyBroadException
            try:
                with mic as source:
                    en.Voice.en("what do You want?")
                    rec.adjust_for_ambient_noise(source, duration=0.5)
                    audio = rec.listen(source)
                    m = rec.recognize_google(audio)
                    en.Voice.en(m)
                    if m.lower() == 'youtube':
                        Y = YouTube
                        Y.YouTube.youtube()
                        break
                    elif m.lower() == 'search':
                        G = Google
                        G.Google.rungoogle()
                        break
                    elif m.lower() == 'exit':
                        en.Voice.en("exit")
                        break
            except Exception:
                en.Voice.en("say again")
    else:
        pass
