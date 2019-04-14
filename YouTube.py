import speech_recognition as sr
from selenium import webdriver
import Voice

mic = sr.Microphone()
rec = sr.Recognizer()


class YouTube:
    @staticmethod
    def youtube():
        while True:
            # noinspection PyBroadException
            try:
                with mic as source:
                    en = Voice
                    en.Voice.en("what you wanna to play?")
                    audio = rec.listen(source)
                    m = rec.recognize_google(audio)
                    en.Voice.en(m)
                    driver = webdriver.Chrome(executable_path="d:\chromedriver.exe")
                    driver.set_page_load_timeout(30)
                    driver.get("https://www.youtube.com")
                    driver.maximize_window()
                    driver.find_element_by_id("search").send_keys(m)
                    driver.find_element_by_id("search-icon-legacy").click()
                    elem = driver.find_elements_by_xpath("/html[1]/body[1]/ytd-app[1]/div[1]/ytd-page-manager["
                                                         "1]/ytd-search[1]/div["
                                                         "1]/ytd-two-column-search-results-renderer[1]/div["
                                                         "1]/ytd-section-list-renderer[1]/div["
                                                         "2]/ytd-item-section-renderer[1]/div[2]/ytd-video-renderer["
                                                         "1]/div[1]/div[1]/div[1]/div[1]/h3[1]/a")
                    print(elem)
                    print(elem.get_attribute("href"))

                    break
            except Exception:
                pass

