import unittest,time,HTMLTestRunner,os,datetime,sys,logging
from config.config_01 import broswer_config
from constant.constant_01 import UFA_HOME_URL,UFA_LOGIN_ADMIN
from util import getReport,sendEmail
from selenium.webdriver.support.select import Select

#sys.path[0]=os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path[0]=os.path.abspath(os.path.dirname(os.getcwd()))
print(sys.path[0])


class LoginAndLogout(unittest.TestCase):
    chrome_driver = 'F:\\tools\\chromedriver.exe'
    browser = broswer_config['chrome'](executable_path=chrome_driver)

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        # self.browser.get(UFA_HOME_URL)
        # self.browser.maximize_window()
        print("setUp")

    def tearDown(self):
        # self.browser.close()
        # self.browser.quit()
        print("tearDown")

    @classmethod
    def tearDownClass(cls):
        pass


    def test_s1_openhomepage(self):
        u"""众家联首页"""
        print("test case1:test_openhomepage")
        self.browser.get(UFA_HOME_URL)
        self.browser.maximize_window()
        title = self.browser.title
        isFlag = False
        if "众家联" in title:
            isFlag = True
        time.sleep(3)
        self.assertEqual(True,isFlag)


    def test_s2_loginportweb_supply(self):
        u"""供应商登录portweb和退出"""
        print("test case1:test_loginportweb")
        self.browser.get(UFA_HOME_URL)
        self.browser.maximize_window()
        #验证是否登录页面
        self.browser.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/div[1]/a[1]").click()
        title = self.browser.title
        isFlag = False
        if "UFA" in title:
            isFlag = True
        time.sleep(3)
        self.browser.find_element_by_id("lccUserName").send_keys("18128682254")
        self.browser.find_element_by_id("lccPassword").send_keys("ufa123")
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div[6]/a').click()
        #检查登录账号昵称是否正确
        nickname = self.browser.find_element_by_xpath("/html/body/header/div[1]/div/div[1]/div[2]/span/a").text
        if not nickname == "18128682254":
            isFlag = False
        #退出登录
        self.browser.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/div[2]/a").click()
        self.assertEqual(True, isFlag)


    def test_s3_loginportweb_purchase(self):
        u"""采购商登录portweb和退出"""
        print("test case1:test_loginportweb")
        self.browser.get(UFA_HOME_URL)
        self.browser.maximize_window()
        #验证是否登录页面
        self.browser.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/div[1]/a[1]").click()
        title = self.browser.title
        isFlag = False
        if "UFA" in title:
            isFlag = True
        time.sleep(3)
        self.browser.find_element_by_id("lccUserName").send_keys("18128682254")
        self.browser.find_element_by_id("lccPassword").send_keys("ufa123")
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div[4]/div[2]').click()
        #选择radio的采购商登录
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div[6]/a').click()
        #检查登录账号昵称是否正确
        nickname = self.browser.find_element_by_xpath("/html/body/header/div[1]/div/div[1]/div[2]/span/a").text
        if not nickname == "18128682254":
            isFlag = False
        #退出登录
        self.browser.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/div[2]/a").click()
        self.assertEqual(True, isFlag)


    def test_s4_loginadmin(self):
        u"""登录admin管理后台"""
        print("test case1:test_loginportweb")
        self.browser.get(UFA_LOGIN_ADMIN)
        self.browser.maximize_window()
        time.sleep(3)
        #验证是否登录页面
        title = self.browser.title
        isFlag = False
        if "UFA" in title:
            isFlag = True
        time.sleep(3)
        #获取验证码
        code1 = self.browser.find_element_by_xpath('//*[@id="formLogin"]/div[4]/div/div/span/span[1]').text
        code2 = self.browser.find_element_by_xpath('//*[@id="formLogin"]/div[4]/div/div/span/span[2]').text
        code3 = self.browser.find_element_by_xpath('//*[@id="formLogin"]/div[4]/div/div/span/span[3]').text
        code4 = self.browser.find_element_by_xpath('//*[@id="formLogin"]/div[4]/div/div/span/span[4]').text
        code = code1 + code2 + code3 + code4
        # 输入帐号密码、验证码
        self.browser.find_element_by_id("username").send_keys("18680409093")
        self.browser.find_element_by_id("password").send_keys("123456")
        self.browser.find_element_by_id("code").send_keys(code)
        self.browser.find_element_by_class_name("submit_btn").click()
        #登录后判断
        admin_title = self.browser.title
        if  not "UFA平台管理中心" in admin_title:
            isFlag = False
        #状态下拉框select选择，企业信息管理
        #self.browser.switch_to.frame(0)
        self.browser.switch_to.frame('ifr_0')
        self.browser.find_element_by_xpath('//*[@id="shortcut"]/div[1]/section/div[2]/dd/a/h3').click() #选择首页--订单管理
        time.sleep(3)
        # self.browser.find_element_by_xpath('//*[@id="larry_left_menu"]/li[2]/a/i').click() #选择一级菜单
        # self.browser.find_element_by_xpath('//*[@id="larry_left_menu"]/li[2]/dl/dd[1]/a/cite').click() #选择二级菜单
        # iframes = self.browser.find_elements_by_tag_name("iframe")
        # for iframe in iframes:
        #     self.browser.switch_to.frame(iframe)
        #     logging.warning(self.browser.title)
        #     if  self.browser.find_element_by_xpath('//*[@id="tableFrom"]/div[1]/div[1]/div[2]/div/div/div/input'):
        #         self.browser.find_element_by_xpath('//*[@id="tableFrom"]/div[1]/div[1]/div[2]/div/div/div/input').click()
        #         self.browser.find_element_by_xpath('//*[@id="tableFrom"]/div[1]/div[1]/div[2]/div/div/dl/dd[4]').click() #选择审核未通过
        #         self.browser.find_element_by_xpath('//*[@id="tableFrom"]/div[1]/div[2]/div[4]/a').click() #点击查询
        #     time.sleep(3)
        self.assertEqual(True, isFlag)
        self.browser.quit()


if __name__ == '__main__':
    #unittest.main()
    # 执行测试用例集并生成报告
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    #suite.addTest(LoginAndLogout("test_openhomepage"))
    #suite.addTest(LoginAndLogout("test_loginportweb_purchase"))
    suite.addTest(LoginAndLogout("test_s4_loginadmin"))
    #生成测试报告
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    dir1 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    dir2 = os.path.join(dir1, 'log')
    filename = os.path.join(dir2, "report" + now + "result.html")
    fp = getReport.MakeReport(filename)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Report_title', description='Report_description')
    runner.run(suite)
    fp.close()
    #sendEmail.SendEmail(filename)