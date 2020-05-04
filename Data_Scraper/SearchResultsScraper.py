import time
from selenium import webdriver

path_to_chrome_webdriver = "C:\\Users\\shahi\\Downloads\\chromedriver_win32\\chromedriver.exe"


class ZipRecruiterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(path_to_chrome_webdriver)
        self.keyword_field = None
        self.location_field = None
        self.submit_button = None
        self.clear_location_button = None

    def go_to_homepage(self):
        self.driver.get("http://www.ziprecruiter.com")

    def set_search(self, search_term,location="Hayward,CA"):
        self.go_to_homepage()
        self.keyword_field = self.driver.find_element_by_id("search1")
        self.keyword_field.send_keys(search_term)
        self.clear_location_button = self.driver.find_element_by_xpath("""//*[@id="search_form_1"]/div[1]/div[2]/button""")
        self.clear_location_button.click()
        self.location_field = self.driver.find_element_by_id("location1")
        self.location_field.send_keys(location)
        self.submit_button = self.driver.find_element_by_class_name("form_submit_wrapper")
        self.submit_button.click()
        time.sleep(1)


    def shutdown(self, delay=5):
        time.sleep(delay)
        self.driver.quit()


# search1, location1
# search_form_1 button
# type = submit, class_="form_submit_wrapper"
Bot = ZipRecruiterBot()

Bot.set_search("Python entry level")

Bot.shutdown(delay=50)
