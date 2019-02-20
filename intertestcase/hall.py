import unittest


import unittest,requests,json,ddt


class MyTestCaseGet(unittest.TestCase):
    def setUp(self):
        print("初始化环境")

    def test_price(self):
        payload = {}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        res = requests.get("https://www.ufa.hk/static/json/chart2.json?_=1523964895384",
                           params=payload,
                           headers=headers)
        print(res.text)

    def tearDown(self):
        print("释放环境")

class MyTestCasePost(unittest.TestCase):
    def setUp(self):
        print("初始化环境")

    def test_price(self):
        headers = {"platform": "android",
                   "timestamp": "1522748144000",
                   "version": "v2.0",
                   "token": "",
                   "sign": "",
                   "Accept": "application/json",
                   "Content-Type": "application/x-www-form-urlencoded"}
        datas = {}
        res = requests.post("https://www.ufa.hk/app-web/deal/findByCategoryTop.pub", data=datas, headers=headers)
        print(res.text)

    def tearDown(self):
        print("释放环境")


if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(MyTestCaseGet)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(MyTestCasePost)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)
