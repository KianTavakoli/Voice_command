import speech_recognition as sr
import Voice

en = Voice
mic = sr.Microphone()
rec = sr.Recognizer()


class Activation:

    @property
    def activate(self='hello'):
        # noinspection PyBroadException
        try:
            en.Voice.en("hello")
            with mic as source:
                rec.adjust_for_ambient_noise(source)
                audio = rec.listen(source)
                transcript = rec.recognize_google(audio)
                print(transcript)
                if transcript.lower() == self:
                    return True
                else:
                    return False
        except Exception:
            en.Voice.en("I didn't hear you")
