import unittest
import requests,json
import ddt

@ddt.ddt
class requestPost(unittest.TestCase):

    def setUp(self):
        print("初始化环境")

    @ddt.data("邱靖雯","邱靖","邱")
    def testPost(self,searchname):
        print("start post api")
        headers={"Content-Type":"application/x-www-form-urlencoded"}
        datas={"feedbackman":searchname}
        res = requests.post("https://www.paison.top/mall-001/trackinglikefeedbackman",
                            data=datas,
                            headers=headers)
        print(res.text)
        print(json.loads(res.text))
        print(json.loads(res.text)[0])
        print(json.loads(res.text)[0]['imgUrl'])
        print(json.loads(res.text)[0]['telephone'])
        print(json.loads(res.text)[0]['tracking'])
        print(json.loads(res.text)[0]['tracking']['id'])
        if u"13418276666" in res.text:
            result = True
            print("pass")
        else:
            result = False
            print("fail")
        self.assertEqual(True, result)

    def testGet(self):
        print("start get api")
        payload ={"city":"北京"}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        res = requests.get("https://www.sojson.com/open/api/weather/xml.shtml",
                           params=payload,
                           headers=headers)
        print(res.text)

    def tearDown(self):
        print("释放环境")


if __name__ == '__main__':
    unittest.main()
