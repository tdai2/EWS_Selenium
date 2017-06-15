#coding=utf-8
import unittest
import time
import HTMLTestRunner
from Testcase import cpuInforCheck,privilegeCheck

testunit =unittest.TestSuite()
testunit.addTest(unittest.makeSuite(cpuInforCheck.cpuInforCheck))
#testunit.addTest(unittest.makeSuite(privilegeCheck.privilegeCheck))
testunit.addTest(privilegeCheck.privilegeCheck("test_add_user"))
testunit.addTest(privilegeCheck.privilegeCheck("test_user_privilege"))
testunit.addTest(privilegeCheck.privilegeCheck("test_operator_privilege"))
testunit.addTest(privilegeCheck.privilegeCheck("test_del_user"))
        
now = time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime(time.time()))
filename = "D:\\learning\\code\\selenium python\\"+now+'result.html'
fp = file(filename,'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title= 'Demo execution',
    description= 'Demo execution'
)
runner.run(testunit)