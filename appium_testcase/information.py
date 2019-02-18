import time
import unittest

from appium import webdriver

from util import getnow


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
        info = self.driver.find_element_by_xpath("//android.widget.TextView[@text='资讯']").click()
        time.sleep(3)
        live = self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.ufa.scm:id/tv_tab_title' and @text='行情直播']").click()
        time.sleep(3)
        headpath = "mallscreenshots/"
        tailpath = ".png"
        gettime = getnow.getnowFunc()
        timepath = headpath + gettime + tailpath
        print("gettime : " + gettime)
        print("timepath : " + timepath)
        self.driver.save_screenshot(timepath)
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.ufa.scm:id/tv_tab_title' and @text='新闻资讯']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id='com.ufa.scm:id/recyclerView']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]").click()
        time.sleep(2)
        content = self.driver.find_element_by_xpath("//android.view.View[@text='2017-2021年中国家具制造行业发展及预测分析']").text
        print("content : " + content)
        if(content == ""):
            result = False
        else:
            result = True
        self.assertEqual(True, result)

    def tearDown(self):
        print("this is tearDown()")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
