import time
from selenium import webdriver
import selenium

path_to_chrome_webdriver = "C:\\Users\\shahi\\Downloads\\chromedriver_win32\\chromedriver.exe"


class ZipRecruiterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(path_to_chrome_webdriver)
        self.driver.get('http://www.ziprecruiter.com')

    def shutdown(self, delay=5):
        time.sleep(delay)
        self.driver.quit()


Bot = ZipRecruiterBot()

Bot.shutdown()