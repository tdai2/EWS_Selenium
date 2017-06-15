# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time



def busy():
    driver = webdriver.Firefox()
    driver.get("www.baidu.com")
    driver.implicitly_wait(5)
    driver.find_element_by_id("LOGIN_VALUE_1").click()
    
    driver.implicitly_wait(5)

def logout(self):
    driver = self.driver
    driver.switch_to_default_content()
    driver.switch_to_frame("header")
    driver.implicitly_wait(5)
    driver.find_element_by_id("_navbarlogouttxt").click()
    self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to log out[\s\S]$")

if __name__ == "__main__":
	busy()


