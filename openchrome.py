from selenium import webdriver
import time,unittest,csv
from ddt import ddt,data,unpack

@ddt
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

    def test_savemysql(self):
        print("test case:test_savemysql")

    @data(("16666666666","ufa123"))
    def test_ddt(self,username):
        print("test case:test_ddt")
        print("username:%(username)s" % {"username":username})

    @data(("16666666666","ufa123",True),("17777777777","ufa123",True),("18680409099","123456",True))
    @unpack
    def test_ddts(self,username,password,expectedresult):
        print("test case:test_ddts")
        print("username:%(username)s--password:%(password)s" % {"username":username,"password":password})

    def test_readcsv(self):
        print("test case:test_readcsv")
        # user_list = csv.reader(open('login.csv','r'))
        # print(user_list)
        # for user in user_list:
        #     print(user[0])
        #     print(user[1])
        #     print(user[2])

    def test_writecsv(self):
        print("test case:test_writecsv")
        user1 = [8,'username1','password1']
        user2 = [9,'username2','password2']
        out = open('login.csv','a',newline='')
        csv_write = csv.writer(out,dialect='excel')
        csv_write.writerow(user1)
        csv_write.writerow(user2)

    # def tearDown(self):
    #     print("tear down testcase")
    # @classmethod
    # def tearDownClass(cls):
    #     print("tear down class testcase")


if __name__ == '__main__':
    unittest.main()
    '''
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase("test_ddt"))
    suite.addTest(MyTestCase("test_ddts"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    '''