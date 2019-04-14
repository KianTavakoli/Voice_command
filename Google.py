
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import Voice

mic = sr.Microphone()
rec = sr.Recognizer()


class Google:

    @staticmethod
    def rungoogle():
        while True:
            # noinspection PyBroadException
            try:
                with mic as source:
                    en = Voice
                    en.Voice.en("ready to search, what you wanna to searching?")
                    audio = rec.listen(source)
                    m = rec.recognize_google(audio)
                    en.Voice.en("You wanna search:")
                    en.Voice.en(m)
                    driver = webdriver.Chrome(executable_path="d:\chromedriver.exe")
                    driver.set_page_load_timeout(30)
                    driver.get("https://www.google.com")
                    driver.maximize_window()
                    search = driver.find_element_by_name('q')
                    search.send_keys(m)
                    search.send_keys(Keys.RETURN)
                    print(search)
                    link = driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[2]/div/div/div[1]/a/h3')
                    print(link)
                    link.clickAndWait()
                    break
            except Exception:
                pass
