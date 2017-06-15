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
import unittest, time, re, os

import configparser as ConfigParser
from functionModule import login,user

class cpuInforCheck(unittest.TestCase):

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

        #CPU information
        self.cpuSocket =cf.get("CPU","Socket")
        self.cpuManufacture =cf.get("CPU","Manufacture")
        self.cpuVersion =cf.get("CPU","Version")
        self.cpuPSignature =cf.get("CPU","Processor Signature")
        self.cpuPType =cf.get("CPU","Processor Type")
        self.cpuFamily =cf.get("CPU","Family")
        self.cpuSpeed =cf.get("CPU","Speed")
        self.cpuCNumber =cf.get("CPU","Number of Cores")
        self.cpuVoltage =cf.get("CPU","Voltage")
        self.cpuSType =cf.get("CPU","Socket Type")
        self.cpuStatus =cf.get("CPU","Status")
        self.cpuSN =cf.get("CPU","Serial Number")
        self.cpuAssetTag =cf.get("CPU","Asset Tag")
        self.cpuPNumber =cf.get("CPU","Part Number")


        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_CPU_infor_heck(self):
        #driver = self.driver
        login.login(self,self.susername,self.suserPassword,self.hostIP,"https")
        driver = self.driver
        #login.login(self,self.susername,self.suserPassword,self.hostIP,"http")
        driver.switch_to.default_content()
        time.sleep(3)
        driver.switch_to.frame("TOPMENU")
        driver.find_element_by_link_text("CPU Information").click()
        #driver.switch_to_default_content()
        driver.switch_to.frame("frame_main")
        self.assertEqual(driver.find_element_by_id("socketNo_0").text, self.cpuSocket , "CPU information Check Fail. Socket Designatin Mismatch")
        self.assertEqual(driver.find_element_by_id("manuf_0").text, self.cpuManufacture , "CPU information Check Fail. Manufacturer Mismatch")
        self.assertEqual(driver.find_element_by_id("version_0").text, self.cpuVersion, "CPU information Check Fail. CPU Version Mismatch")
        self.assertEqual(driver.find_element_by_id("procSig_0").text, self.cpuPSignature , "CPU information Check Fail. CPU Signature Mismatch")
        self.assertEqual(driver.find_element_by_id("procType_0").text, self.cpuPType, "CPU information Check Fail. CPU Type Mismatch")
        self.assertEqual(driver.find_element_by_id("procFamily_0").text, self.cpuFamily , "CPU information Check Fail. CPU Type Mismatch")
        self.assertEqual(driver.find_element_by_id("speed_0").text, self.cpuSpeed , "CPU information Check Fail. CPU Speed Mismatch")
        self.assertEqual(driver.find_element_by_id("cores_0").text, self.cpuCNumber , "CPU information Check Fail. CPU Core Number Mismatch")
        self.assertEqual(driver.find_element_by_id("voltage_0").text, self.cpuVoltage, "CPU information Check Fail. CPU Voltage Mismatch")
        self.assertEqual(driver.find_element_by_id("socketType_0").text, self.cpuSType , "CPU information Check Fail. CPU Socket type Mismatch")
        self.assertEqual(driver.find_element_by_id("status_0").text, self.cpuStatus, "CPU information Check Fail. CPU Status Mismatch")
        self.assertEqual(driver.find_element_by_id("serialNo_0").text, self.cpuSN , "CPU information Check Fail. CPU Serial Number Mismatch")
        self.assertEqual(driver.find_element_by_id("assetTag_0").text, self.cpuAssetTag , "CPU information Check Fail. CPU Asset Tag Mismatch")
        self.assertEqual(driver.find_element_by_id("partNo_0").text, self.cpuPNumber , "CPU information Check Fail. CPU Part Number Mismatch")
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
    pwd = os.path.abspath('.')
    os.chdir(pwd)
    unittest.main()



