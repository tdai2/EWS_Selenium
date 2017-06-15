# -*- coding: utf-8 -*-
import os,os.path,sys
#print("Before append path of file:"+__file__+". The sys path is:")
#print(sys.path)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time
import unittest


def login(self,uname,password,IP,protocol):
    driver = self.driver
    base = protocol+"://"+IP
    check = driver.get(base)
    driver.find_element_by_name("name").clear()
    driver.find_element_by_name("name").send_keys(uname)
    driver.find_element_by_name("pwd").clear()
    driver.find_element_by_name("pwd").send_keys(password)
    driver.find_element_by_id("loginbtn").click()
def logout(self):
    driver = self.driver
    driver.switch_to_default_content()
    time.sleep(2)
    driver.switch_to_frame("TOPMENU")
    driver.find_element_by_id("_headerlogouttxt").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']/button[2]/span").click()
    #self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to log out")
    driver.close()


class loginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.accept_next_alert = True
    def test_log_in(self):
        login(self,"root","superuser","10.239.55.128","http")
        logout(self)
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True


if __name__ == "__main__":
    unittest.main()



