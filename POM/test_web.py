#this page contains the webpage test that checks the webpage url to ensure that the url changes to the quiz page

import random
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from web_locators import Pg_locators

class Quiz_Results(unittest.TestCase):
    pageURL = "https://www.albany.edu/~BP754362/tips.html"
    driver = webdriver.Chrome("/Users/briana/Desktop/chromedriver")

    #generates random number to insert in quiz answers
    num = list(range(1,11))
    random_num = random.choice(num)

    def setUp(self):
        self.driver.get(self.pageURL)
        self.driver.maximize_window()
        time.sleep(5)
    
    def test_quiz(self):
        loc = Pg_locators()
        #clicks on quiz page
        loc.page_link_txt1 = self.driver.find_element_by_link_text(loc.page_link_txt).click()
        time.sleep(5)
        loc.question1 = self.driver.find_element_by_id(loc.q1).send_keys(self.random_num)
        time.sleep(5)
        loc.question2 = self.driver.find_element_by_id(loc.q2).send_keys(self.random_num)
        time.sleep(5)
        loc.question3 = self.driver.find_element_by_id(loc.q3).send_keys(self.random_num)
        time.sleep(5)
        loc.question4 = self.driver.find_element_by_id(loc.q4).send_keys(self.random_num)
        time.sleep(5)
        loc.question5 = self.driver.find_element_by_id(loc.q5).send_keys(self.random_num)
        time.sleep(5)
        loc.click_btn = self.driver.find_element_by_xpath(loc.calc_btn_xpath).click()
        time.sleep(5)

        expectedURL = "https://www.albany.edu/~BP754362/stressquiz.html"
       #Checks if url has changed to the quiz page
        if self.driver.current_url == expectedURL:
            time.sleep(1)
            print("True")
        else:
            print("False")

    def tearDown(cls):
        cls.driver.close()
if __name__ == "__main__":
    unittest.main()

    


        
        
