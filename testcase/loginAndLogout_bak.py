from selenium import webdriver
import unittest,time,csv
from ddt import ddt,data,unpack
import string


class LoginAndLogout(unittest.TestCase):
    chrome_driver = 'F:\\tools\\chromedriver.exe'
    browser = webdriver.Chrome(executable_path=chrome_driver)

    def setUp(self):
        self.browser.get("https://www.ufa.hk")
        self.browser.maximize_window()

    def tearDown(self):
        self.browser.quit()

    def test_openhomepage(self):
        print("test case1:test_openhomepage")
        title = self.browser.title
        isFlag = False
        if "众家联" in title:
            isFlag = True
            print("isFlag 1 : " + str(22222))
        print(title.find("众家联"))
        print("title = " + title)
        time.sleep(3)
        self.assertEqual(True,isFlag)


if __name__ == '__main__':
    unittest.main()