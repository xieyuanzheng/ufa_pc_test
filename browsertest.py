from selenium import webdriver
import time,unittest

# print("test case:test_savecsv")
# chrome_driver = 'F:\\tools\\chromedriver.exe'
# browser = webdriver.Chrome(executable_path=chrome_driver)
# browser.get("https://www.baidu.com")
# browser.maximize_window()
# time.sleep(3)
# browser.quit()

class MyTestCase(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     print("set up class testcase")
    # def setUp(self):
    #     print("set up testcase")

    def test_savecsv(self):
        print("test case:test_savecsv")
        '''
        chrome_driver = 'F:\\tools\\chromedriver.exe'
        browser = webdriver.Chrome(executable_path=chrome_driver)
        browser.get("https://www.baidu.com")
        browser.maximize_window()
        time.sleep(5)
        browser.quit()'''


if __name__ == '__main__':
    unittest.main()
    '''
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase("test_ddt"))
    suite.addTest(MyTestCase("test_ddts"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    '''