#coding=utf-8
import os,os.path,sys
#print("Before append path of file:"+__file__+". The sys path is:")
#print(sys.path)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import unittest
import time
from Testcase.functionModule import Py3HTMLTestRunner as Py3ReportGenerator
from Testcase import cpuInforCheck
from Testcase import privilegeCheck
import webbrowser


testunit =unittest.TestSuite()
testunit.addTest(unittest.makeSuite(cpuInforCheck.cpuInforCheck))
testunit.addTest(privilegeCheck.privilegeCheck("test_add_user"))
testunit.addTest(privilegeCheck.privilegeCheck("test_del_user"))
pwd = os.path.abspath('.')
now = time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime(time.time()))
filename = now+'result.html'
filename = os.path.join(pwd,'Testlog',filename)
fp = open(filename,'wb')
runner = Py3ReportGenerator.HTMLTestRunner(
    stream=fp,
    title= 'Demo execution',
    description= 'Demo execution'
)
runner.run(testunit)
webbrowser.open("file:///"+filename,new=0)


