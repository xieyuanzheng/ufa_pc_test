#encoding:utf-8
import unittest,time,os
from appium import webdriver
from ddt import ddt,data,unpack


class MyTestCase(unittest.TestCase):

    def setUp(self):
        print("this is setUp()")
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.1'
        desired_caps['deviceName'] = 'I7EUIJORE6YTKVR8'
        desired_caps['appPackage'] = 'com.ufa.scm'
        desired_caps['appActivity'] = '.mvp.main.MainActivity'
        # desired_caps['appActivity'] = '.mvp.splash.GuideActivity'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_something(self):
        time.sleep(3)
        self.driver.swipe(540, 550, 540, 1050)
        time.sleep(3)
        self.driver.find_element_by_id("tv_search").click()
        self.driver.find_element_by_id("et_search").send_keys("一分钱")
        time.sleep(3)
        os.system("adb shell ime set com.sohu.inputmethod.sogou.vivo/.SogouIME")
        time.sleep(3)
        self.driver.find_element_by_id("et_search").click()
        self.driver.press_keycode(66)
        time.sleep(3)
        os.system("adb shell ime set io.appium.android.ime/.UnicodeIME")
        time.sleep(3)
        self.assertEqual(True, True)



    def tearDown(self):
        print("this is tearDown()")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
