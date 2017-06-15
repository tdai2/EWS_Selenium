# -*- coding: utf-8 -*-
import sys,os,os.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#print(sys.path)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import configparser as ConfigParser
import time
import functionModule.login as login


def addUser(self,uname,upassword,utype,uID):
        driver = self.driver
        #login.login(self,self.susername,self.suserPassword,self.hostIP,"http")
        driver.switch_to_default_content()
        time.sleep(2)
        driver.switch_to.frame("TOPMENU")
        driver.find_element_by_id("configuration").click()
        time.sleep(1)
        driver.find_element_by_link_text("Users").click()
        time.sleep(1)
        driver.switch_to_frame("frame_main")
        driver.find_element_by_xpath("//td[contains(text(),'~')]").click()
        driver.find_element_by_id("btn_add").click()
        #driver.switch_to.frame("frame_main")
        driver.find_element_by_id("text_name").clear()
        driver.find_element_by_id("text_name").send_keys(uname)
        driver.find_element_by_id("password_pwd").clear()
        driver.find_element_by_id("password_pwd").send_keys(upassword)
        driver.find_element_by_id("password_pwd_check").clear()
        driver.find_element_by_id("password_pwd_check").send_keys(upassword)
        #driver.find_element_by_id("select_priv")
        #driver.find_element_by_xpath("//option[@value='3']").click();
        selectPrivilege = Select(driver.find_element_by_id("select_priv"))
        selectPrivilege.select_by_index(utype)
        driver.find_element_by_id("btn_add").click()
        time.sleep(1)
        #driver.switch_to.frame("TOPMENU")
        driver.find_element_by_xpath("//span[@id='ui-id-1']/../button").click()

        return self.assertEqual("User was added successfully", "User was added successfully")

def delPrilegeCheck(self):
        driver = self.driver
        driver.switch_to_default_content()
        time.sleep(2)
        driver.switch_to_frame("header")
        driver.find_element_by_link_text("Configuration").click()

        driver.switch_to_default_content()
        time.sleep(2)
        driver.switch_to_frame("sidebar")
        driver.find_element_by_link_text("Users").click()

        driver.switch_to_default_content()
        time.sleep(2)
        driver.switch_to_frame("mainFrame")
        if driver.find_element_by_id("_delUser").get_attribute("disabled") =="true":
                return "No privilege"

def navToConfigUsers(self):
        driver = self.driver
        driver.switch_to_default_content()
        time.sleep(2)
        driver.switch_to_frame("header")
        driver.find_element_by_link_text("Configuration").click()

        driver.switch_to_default_content()
        time.sleep(2)
        driver.switch_to_frame("sidebar")
        driver.find_element_by_link_text("Users").click()

        driver.switch_to_default_content()
        time.sleep(2)
        driver.switch_to_frame("mainFrame")
        k = driver.find_element_by_xpath("//html/body/p").text
        if k=="This user does not have sufficient privilege to view this page.":
                return "User"
        return "NotUser"

def navToConfigNM(self):
        driver = self.driver
        driver.switch_to_default_content()
        time.sleep(2)
        driver.switch_to_frame("header")
        driver.find_element_by_link_text("Configuration").click()

        driver.switch_to_default_content()
        time.sleep(2)
        driver.switch_to_frame("sidebar")
        driver.find_element_by_link_text("Node Manager").click()

        driver.switch_to_default_content()
        time.sleep(2)
        driver.switch_to_frame("mainFrame")
        k = driver.find_element_by_xpath("//html/body/p").text
        if k=="This user does not have sufficient privilege to view this page.":
                return "User"
        return "NotUser"
            #== "This user does not have sufficient privilege to view this page."

#def navTo(top):

def delUserByName(self,uname):
        driver = self.driver
        driver.switch_to_default_content()
        time.sleep(2)
        driver.switch_to.frame("TOPMENU")
        driver.find_element_by_id("configuration").click()
        time.sleep(1)
        driver.find_element_by_link_text("Users").click()
        time.sleep(1)
        driver.switch_to_frame("frame_main")
        driver.find_element_by_xpath("//td[contains(text(),'%s')]"%uname).click()
        driver.find_element_by_id("btn_del").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']/button[2]/span").click()
        time.sleep(20)
        driver.find_element_by_xpath("//span[@id='ui-id-2']/../button").click()
        self.assertEqual("User has been deleted", "User has been deleted")

