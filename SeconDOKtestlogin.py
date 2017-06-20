# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class (unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_(self):
        success = True
        wd = self.wd
        wd.get("http://www.secondok.com/test")
        wd.find_element_by_id("log_email").click()
        wd.find_element_by_id("log_email").clear()
        wd.find_element_by_id("log_email").send_keys("dmitriy115@i.ua")
        wd.find_element_by_css_selector("span.ng-binding").click()
        wd.find_element_by_xpath("//div[@class='small_cont']//span[.='Your password']").click()
        wd.find_element_by_id("log_pwd").click()
        wd.find_element_by_id("log_pwd").clear()
        wd.find_element_by_id("log_pwd").send_keys("12345678")
        wd.find_element_by_xpath("//div[@class='small_cont']//div[.='Enter to the account']").click()
        wd.find_element_by_xpath("//div[@class='h_actions']/a[1]").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
