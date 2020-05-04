import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path_to_chrome_webdriver = "C:\\Users\\shahi\\Downloads\\chromedriver_win32\\chromedriver.exe"


class ZipRecruiterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(path_to_chrome_webdriver)

    def go_to_homepage(self):
        self.driver.get("http://www.ziprecruiter.com")

    def set_search(self, search_term,location="Hayward,CA"):
        self.go_to_homepage()
        keyword_field = self.driver.find_element_by_id("search1")
        keyword_field.send_keys(search_term)
        clear_location_button = self.driver.find_element_by_xpath("""//*[@id="search_form_1"]/div[1]/div[2]/button""")
        clear_location_button.click()
        location_field = self.driver.find_element_by_id("location1")
        location_field.send_keys(location + Keys.ENTER)
        time.sleep(1)
        self.close_search_popup()

    def shutdown(self, delay=5):
        for i in range(delay):
            print("Shutdown in {} seconds".format(delay-i))
            time.sleep(1)
        self.driver.quit()

    def close_search_popup(self):
        url = self.driver.current_url
        url = url + "#primary"
        time.sleep(2)
        self.driver.get(url)
        self.driver.refresh()

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def load_all_search_results(self):
        self.scroll_to_bottom()
        load_jobs_button = self.driver.find_element_by_xpath("""//*[@id="primary"]/section[2]/div/button""")
        load_jobs_button.click()
        last_height = 0
        while True:
            time.sleep(1)
            self.scroll_to_bottom()
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("All results loaded!")
                break
            last_height = new_height

    def return_all_job_postings(self):
        full_list = []
        all_posts = self.driver.find_elements_by_class_name("job_link")
        for post in all_posts:
            link = post.get_attribute("href")
            full_list.append(link)
        print(full_list)
        return full_list

