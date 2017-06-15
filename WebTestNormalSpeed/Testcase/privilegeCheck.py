# -*- coding: utf-8 -*-
import os,os.path,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

import configparser as ConfigParser
from functionModule import login,user

class privilegeCheck(unittest.TestCase):

    def setUp(self):
        cf = ConfigParser.ConfigParser()
        pwd = os.path.abspath(__file__)
        pwd = os.path.dirname(pwd)
        pwd = os.path.join(pwd,"config.ini")
        cf.read(pwd)

        self.hostIP = cf.get("SUT","channel1IP")
        self.susername = cf.get("SUT","susername")
        self.suserPassword = cf.get("SUT","suserPassword")
        self.ousername = cf.get("SUT","ousername")
        self.ouserPassword = cf.get("SUT", "ouserPassword" )
        self.uusername = cf.get("SUT","uusername")
        self.uuserPassword = cf.get("SUT", "uuserPassword" )

        self.uADMIN = cf.get("EWS","administrator")
        self.uOPERATOR = cf.get("EWS","operator")
        self.uUSER = cf.get("EWS","user")
        self.uCALLBACK = cf.get("EWS","callback")
        self.uNoACCESS =cf.get("EWS","noAccess")

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add_user(self):
        login.login(self,self.susername,self.suserPassword,self.hostIP,"https")
        user.addUser(self,"adduser","password",self.uOPERATOR,6)
        user.addUser(self,"user2","password",self.uUSER,8)
        login.logout(self)

    def test_del_user(self):
        login.login(self,self.susername,self.suserPassword,self.hostIP,"https")
        user.delUserByName(self,"adduser")
        user.delUserByName(self,"user2")
        login.logout(self)


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    pwd = os.path.abspath('..')
    os.chdir(pwd)
    unittest.main()
