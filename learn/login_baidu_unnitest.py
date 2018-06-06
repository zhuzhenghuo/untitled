import time

from selenium import webdriver
import unittest

from selenium.webdriver.support.select import Select


class LoginBaidu(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.url="http://ts.zhaopin.com/jump/index_new.html"
        self.browser.implicitly_wait(30)


    def tearDown(self):
        self.browser.quit()

    def test_baidu(self):
        browser=self.browser
        browser.get(self.url)
        browser.find_element_by_id("login_name").send_keys("admin")
        browser.find_element_by_id("login_password").send_keys("admin")



        browser.find_element_by_id("sb_form_q").send_keys("鲁迅")
        browser.find_element_by_id("sb_form_go").click()
        time.sleep(10)
        self.assertIn("登录",browser.page_source)
        self.assertIn("bing",browser.current_url)

if __name__ == "__main__":
    unittest.main()



