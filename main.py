import unittest,time,HTMLTestRunner,os,datetime,sys
from config.config_01 import broswer_config
from constant.constant_01 import UFA_HOME_URL
from util import getReport,sendEmail
from testcase.loginAndLogout import LoginAndLogout


if __name__ == '__main__':
    #unittest.main()
    # 执行测试用例集并生成报告
    # suite = unittest.TestSuite()
    # suite.addTest(LoginAndLogout("test_openhomepage"))
    # runner = unittest.TextTestRunner()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(LoginAndLogout)
    suite = unittest.TestSuite([suite1])
    runner = unittest.TextTestRunner(verbosity=2)
    print("--------------------")
    #生成测试报告
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    dir1 = os.path.abspath(os.path.dirname(__file__))
    dir2 = os.path.join(dir1, 'log')
    filename = os.path.join(dir2, "report" + now + "result.html")
    fp = getReport.MakeReport(filename)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='UFA自动化', description='众家联PC端自动化测试报告')
    result = runner.run(suite)
    testResult = HTMLTestRunner._TestResult()
    runNumber = int(str(result)[str(result).find('run')+4])
    errorNumber = int(str(result)[str(result).find('errors') + 7])
    failuresNumber = int(str(result)[str(result).find('failures') + 9])
    fp.close()
    if errorNumber>0 or failuresNumber>0:
        text = "自动化测试用例失败，网站无法打开，请及时定位，其中：error="+str(errorNumber) +"; failure="+str(failuresNumber)
        sendEmail.SendEmail(filename,text)
    else:
        text = "自动化测试用例正常，网站正常打开。本次是测试邮件，以后会在异常的时候再发邮件。每天8点和14点自动执行一次"
        #sendEmail.SendEmail(filename, text)