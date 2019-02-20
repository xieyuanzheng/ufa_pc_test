#encoding:utf-8

from appium import webdriver
import time,unittest
from ddt import ddt,data,unpack

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("#脚本初始化,获取操作实例")
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.1'
        desired_caps['deviceName'] = 'I7EUIJORE6YTKVR8'
        desired_caps['appPackage'] = 'com.ufa.scm'
        desired_caps['appActivity'] = '.mvp.main.MainActivity'
        #desired_caps['appActivity'] = '.mvp.splash.GuideActivity'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboadr'] = 'True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def tearDown(self):
        print("#释放资源")
        self.driver.quit()

    def testSplash(self):
        print("hello world")
        time.sleep(3)
        self.driver.swipe(540,550,540,1050)
        time.sleep(3)
        print(self.driver.find_element_by_xpath("//android.widget.TextView[@text='我的']").text)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='我的']").click()
        time.sleep(3)


    @data(("16666666666","ufa123",True),("17777777777","ufa123",True),("18680409099","123456",True))
    @unpack
    def testLoginIn(self,username,password,expectedresult):
        print("start testLoginIn testing")
        time.sleep(3)
        self.driver.swipe(540, 550, 540, 1050)
        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='我的']").click()
        #self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.TextView[1]").click()
        #self.driver.find_element_by_android_uiautomator("new UiSelector().text(\'+我的\')")
        #登录
        self.driver.find_element_by_id("tv_login").click()
        self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.ufa.scm:id/et_input' and @text='请输入登录账号']").send_keys(username)
        self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.ufa.scm:id/et_input' and @text='请输入密码']").send_keys(password)
        self.driver.find_element_by_id("btn_login").click()
        if self.driver.find_element_by_id("iv_setting").is_displayed():
            exist = True
        else:
            exist = False
        #退出登录
        self.driver.find_element_by_id("iv_setting").click()
        self.driver.find_element_by_id("tv_logout").click()
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        print("width: " ,width)
        print("height: " ,height)
        print("current activity:",self.driver.current_activity)
        self.driver.save_screenshot('D:/Projects/Python Project/ufatest/screenshot/foo.png')
        self.assertEqual(exist,expectedresult)
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
    '''
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase('testLoginIn'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite) '''
