import unittest,time,HTMLTestRunner,os,datetime,sys
from config.config_01 import broswer_config
from constant.constant_01 import UFA_HOME_URL
from util import getReport,sendEmail
from testcase.loginAndLogout import LoginAndLogout
from testcase.homeLink import HomeLinkAndDetailSD,HomeLinkAndDetailInfo,HomeLinkAndDetailVideo
from testcase.search import GoodsSearch,StoreSearch
from testcase.mallpost import MyTestCase
from log.log import log1

if __name__ == '__main__':
    log1.info("开始测试")
    #unittest.main()
    # 执行测试用例集并生成报告
    # suite = unittest.TestSuite()
    # suite.addTest(HomeLinkAndDetail("test_s1_supplyAndDemand"))
    # suite.addTest(HomeLinkAndDetailInfo("test_s2_information"))
    # suite.addTest(HomeLinkAndDetailVideo("test_s3_video"))
    # runner = unittest.TextTestRunner()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(LoginAndLogout)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(HomeLinkAndDetailSD)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(HomeLinkAndDetailInfo)
    suite4 = unittest.TestLoader().loadTestsFromTestCase(HomeLinkAndDetailVideo)
    suite5 = unittest.TestLoader().loadTestsFromTestCase(GoodsSearch)
    suite6 = unittest.TestLoader().loadTestsFromTestCase(StoreSearch)
    suite7 = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    suite = unittest.TestSuite([suite1,suite2,suite3,suite4,suite5,suite6,suite7])
    runner = unittest.TextTestRunner(verbosity=2)
    print("--------------------")
    #生成测试报告
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    now_hour = time.strftime("%Y-%m-%d-%H", time.localtime(time.time()))
    dir1 = os.path.abspath(os.path.dirname(__file__))
    dir2 = os.path.join(dir1, 'log')
    dir2 = os.path.join(dir2, 'report')
    html_filename = os.path.join(dir2, "report" + now + "result.html")
    picture_name = os.path.join(os.path.join(dir1,'screenshot'),now_hour+".jpg")
    listpart = [html_filename,picture_name]
    fp = getReport.MakeReport(html_filename)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='UFA自动化', description='众家联PC端自动化测试报告')
    result = runner.run(suite)
    testResult = HTMLTestRunner._TestResult()
    runNumber = int(str(result)[str(result).find('run')+4])
    errorNumber = int(str(result)[str(result).find('errors') + 7])
    failuresNumber = int(str(result)[str(result).find('failures') + 9])
    fp.close()
    to_addr_list = ['121546683@qq.com']
    #to_addr_list = ['4141847@qq.com', '121546683@qq.com','76656630@qq.com','181643605@qq.com','368422559@qq.com','297086499@qq.com']
    if errorNumber>0 or failuresNumber>0:
        text = "自动化测试用例失败，请及时定位，其中：运行用例数="+str(runNumber) + "; error="+str(errorNumber) +"; failure="+str(failuresNumber)
        sendEmail.SendEmail(listpart,text,to_addr_list)
    else:
        text = "自动化测试用例正常，网站正常打开。本次是测试邮件，以后会在异常的时候再发邮件。每天8点和14点自动执行一次"
        #sendEmail.SendEmail(listpart, text,to_addr_list)
    log1.info("end")