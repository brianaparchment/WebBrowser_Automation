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

