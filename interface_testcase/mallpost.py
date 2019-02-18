import unittest,requests,json,ddt
from config import config_headers
import pymysql
from util import opt_db

class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("初始化环境")

    #搜索店铺
    def test_searchStore(self):
        headers = config_headers.headers_config
        datas = {"sk":"", "pageNo":"1","pageSize":"10"}
        res = requests.post("https://www.ufa.hk/app-web/shop/searchStore.pub",data=datas,headers=headers)
        print("搜索店铺 : test_searchStore")
        #操作数据库
        # print(opt_db.fetchone_mysql())
        sql = "SELECT * from interfacetestcase.author"
        print(opt_db.fetchall_mysql(sql)[4][3])
        # print(json.loads(res.text)["msg"])
        # print(json.loads(res.text)["data"]["page"]["totalSize"])
        # print(json.loads(res.text)["data"]["list"][0]["goods"][0]["name"])
        list_len = len(json.loads(res.text)["data"]["list"])
        for i in range(list_len):
            goods_len = len(json.loads(res.text)["data"]["list"][i]["goods"])
            for j in range(goods_len):
                #print(json.loads(res.text)["data"]["list"][i]["goods"][j]["name"])
                pass
        if json.loads(res.text)["msg"] == "SUCCESS" :
            print("test_searchStore is ok!")
            #print(res.headers)
            result = True
        else:
            print("test_searchStore is fail!")
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
    #unittest.main
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase("test_searchStore"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
