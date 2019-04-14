import pyttsx3


class Voice:
    @staticmethod
    def en(x):
        engine = pyttsx3.init()
        engine.setProperty('volume', 0.9)  # Volume 0-1
        engine.say(x)
        engine.runAndWait()
