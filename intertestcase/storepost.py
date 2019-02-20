import unittest,requests,json,ddt


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("初始化环境")


    def test_storeHome(self):
        """店铺首页"""
        headers = {"platform": "android",
                   "timestamp": "1522748144000",
                   "version": "v2.0",
                   "token": "",
                   "sign": "",
                   "Accept": "application/json",
                   "Content-Type": "application/x-www-form-urlencoded"}
        datas = {"stoId":"2110000000000083"}
        res = requests.post("https://www.ufa.hk/app-web/store/storeHome.pub", data=datas, headers=headers)
        print(res.text)
        print(res.status_code)
        print(res.headers)
        print(res.encoding)
        print(res.cookies)
        if json.loads(res.text)["msg"] == "SUCCESS":
            result = True
        else:
            result = False
        self.assertEqual(True, result)


    def test_storeAbout(self):
        """企业介绍与联系方式"""
        headers = {"platform": "android",
                   "timestamp": "1522748144000",
                   "version": "v2.0",
                   "token": "",
                   "sign": "",
                   "Accept": "application/json",
                   "Content-Type": "application/x-www-form-urlencoded"}
        datas = {"stoId": "2110000000000083"}
        res = requests.post("https://www.ufa.hk/app-web/store/storeAbout.pub", data=datas, headers=headers)
        print(res.text)
        if json.loads(res.text)["msg"] == "SUCCESS":
            result = True
        else:
            result = False
        self.assertEqual(True, result)


    def test_proSort(self):
        """产品分类"""
        headers = {"platform": "android",
                   "timestamp": "1522748144000",
                   "version": "v2.0",
                   "token": "",
                   "sign": "",
                   "Accept": "application/json",
                   "Content-Type": "application/x-www-form-urlencoded"}
        datas = {"stoId": "2110000000000083"}
        res = requests.post("https://www.ufa.hk/app-web/store/proSort.pub", data=datas, headers=headers)
        print(res.text)
        if json.loads(res.text)["msg"] == "SUCCESS":
            result = True
        else:
            result = False
        self.assertEqual(True, result)


    def test_proList(self):
        """全部产品"""
        headers = {"platform": "android",
                   "timestamp": "1522748144000",
                   "version": "v2.0",
                   "token": "",
                   "sign": "",
                   "Accept": "application/json",
                   "Content-Type": "application/x-www-form-urlencoded"}
        datas = {"stoId": "2110000000000083","pageNo":"1","pageSize":"10"}
        res = requests.post("https://www.ufa.hk/app-web/store/proList.pub", data=datas, headers=headers)
        print(res.text)
        if json.loads(res.text)["msg"] == "SUCCESS":
            result = True
        else:
            result = False
        self.assertEqual(True, result)


    def test_storeAlbum(self):
        """店铺相册"""
        headers = {"platform": "android",
                   "timestamp": "1522748144000",
                   "version": "v2.0",
                   "token": "",
                   "sign": "",
                   "Accept": "application/json",
                   "Content-Type": "application/x-www-form-urlencoded"}
        datas = {"stoId": "2110000000000083", "pageNo": "1", "pageSize": "10"}
        res = requests.post("https://www.ufa.hk/app-web/store/storeAlbum.pub", data=datas, headers=headers)
        print(res.text)
        if json.loads(res.text)["msg"] == "SUCCESS":
            result = True
        else:
            result = False
        self.assertEqual(True, result)


    def test_albumDetail(self):
        """相册详情"""
        headers = {"platform": "android",
                   "timestamp": "1522748144000",
                   "version": "v2.0",
                   "token": "",
                   "sign": "",
                   "Accept": "application/json",
                   "Content-Type": "application/x-www-form-urlencoded"}
        datas = {"abmId": "2701256941944832", "pageNo": "1", "pageSize": "10"}
        res = requests.post("https://www.ufa.hk/app-web/store/albumDetail.pub", data=datas, headers=headers)
        print(res.text)
        if json.loads(res.text)["msg"] == "SUCCESS":
            result = True
        else:
            result = False
        self.assertEqual(True, result)


    def test_news(self):
        """企业动态"""
        headers = {"platform": "android",
                   "timestamp": "1522748144000",
                   "version": "v2.0",
                   "token": "",
                   "sign": "",
                   "Accept": "application/json",
                   "Content-Type": "application/x-www-form-urlencoded"}
        datas = {"stoId": "2110000000000083", "pageNo": "1", "pageSize": "10"}
        res = requests.post("https://www.ufa.hk/app-web/store/news.pub", data=datas, headers=headers)
        print(res.text)
        if json.loads(res.text)["msg"] == "SUCCESS":
            result = True
        else:
            result = False
        self.assertEqual(True, result)


    def test_storeHead(self):
        """店铺头部"""
        headers = {"platform": "android",
                   "timestamp": "1522748144000",
                   "version": "v2.0",
                   "token": "",
                   "sign": "",
                   "Accept": "application/json",
                   "Content-Type": "application/x-www-form-urlencoded"}
        datas = {"stoId": "2110000000000083"}
        res = requests.post("https://www.ufa.hk/app-web/store/storeHead.pub", data=datas, headers=headers)
        print(res.text)
        if json.loads(res.text)["msg"] == "SUCCESS":
            result = True
        else:
            result = False
        self.assertEqual(True, result)

    def tearDown(self):
        print("释放环境")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase("test_storeHome"))
    suite.addTest(MyTestCase("test_storeAbout"))
    suite.addTest(MyTestCase("test_proSort"))
    suite.addTest(MyTestCase("test_proList"))
    suite.addTest(MyTestCase("test_storeAlbum"))
    suite.addTest(MyTestCase("test_albumDetail"))
    suite.addTest(MyTestCase("test_news"))
    suite.addTest(MyTestCase("test_storeHead"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
