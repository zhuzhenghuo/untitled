import time
import unittest
import ddt
from selenium import webdriver
testdate=[["zzh","nishi369","退出"],
          ["heheh","111","登录失败"],
          ["","1123","请检查您的用户名"]]

@ddt.ddt
class RanZhiAdminLogin(unittest.TestCase):

    def setUp(self):
        self.broser=webdriver.Firefox()
        self.url="http://www.ranzhi.org/user-login.html"
        self.broser.implicitly_wait(30)

    def tearDown(self):
        self.browser.quit()


    @ddt.unpack
    @ddt.data(*testdate)
    def test_adminlogin(self,admin,password,log):
        '''admin 登录正确的用例'''
        broser=self.broser
        broser.get(self.url)
        time.sleep(2)
        broser.find_element_by_xpath('//*[@id="account"]').send_keys(admin)
        time.sleep(2)
        broser.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        time.sleep(2)
        broser.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(3)
        self.assertIn(log,broser.page_source)


if __name__ =="__main__":
    unittest.main()