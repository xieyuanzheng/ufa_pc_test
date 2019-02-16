import unittest,requests,json,ddt

class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("初始化环境")

    #搜索店铺
    def test_searchStore(self):
        headers = {"platform":"android",
                   "timestamp":"1522748144000",
                   "version":"v2.0",
                   "token":"",
                   "sign":"",
                   "Accept":"application/json",
                   "Content-Type":"application/x-www-form-urlencoded"}
        datas = {"sk":"", "pageNo":"1","pageSize":"10"}
        res = requests.post("https://www.ufa.hk/app-web/shop/searchStore.pub",data=datas,headers=headers)
        print(res.text)
        if json.loads(res.text)["msg"] == "SUCCESS" :
            print("test_searchStore")
            result = True
        else:
            result = False
        self.assertEqual(True, result)

    #商品搜索
    def test_searchGoods(self):
        headers = {"platform": "android",
                   "timestamp": "1522748144000",
                   "version": "v2.0",
                   "token": "",
                   "sign": "",
                   "Accept": "application/json",
                   "Content-Type": "application/x-www-form-urlencoded"}
        datas = {"pageNo":"1","pageSize":"10"}
        res = requests.post("https://www.ufa.hk/app-web/shop/searchGoods.pub",data=datas,headers=headers)
        print(res.text)
        if json.loads(res.text)["msg"] == "SUCCESS" :
            print("test_searchGoods")
            result = True
        else:
            result = False
        self.assertEqual(True,result)

    #商品首页—产品分类，级联三级
    def test_gdsType(self):
        headers = {"platform": "android",
                   "timestamp": "1522748144000",
                   "version": "v2.0",
                   "token": "",
                   "sign": "",
                   "Accept": "application/json",
                   "Content-Type": "application/x-www-form-urlencoded"}
        datas = {}
        res = requests.post("https://www.ufa.hk/app-web/shop/searchGoods.pub",data=datas,headers=headers)
        print(res.text)
        if json.loads(res.text)["msg"] == "SUCCESS" :
            print("test_gdsType")
            result = True
        else:
            result = False
        self.assertEqual(True,result)

    #商城首页：主题市场-优质商家-新品专区-产品推荐-广告图-众家头条
    def test_themeMarket(self):
        headers = {"platform": "android",
                   "timestamp": "1522748144000",
                   "version": "v2.0",
                   "token": "",
                   "sign": "",
                   "Accept": "application/json",
                   "Content-Type": "application/x-www-form-urlencoded"}
        datas = {}
        res = requests.post("https://www.ufa.hk/app-web/gds/themeMarket.pub",data=datas,headers=headers)
        print(res.text)
        if json.loads(res.text)["msg"] == "SUCCESS" :
            print("test_themeMarket")
            result = True
        else:
            result = False
        self.assertEqual(True,result)

    def tearDown(self):
        print("释放环境")

if __name__ == '__main__':
    unittest.main
