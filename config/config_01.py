from selenium import webdriver
import time


# 浏览器种类维护在此处
broswer_config = {
    'ie' : webdriver.Ie,
    'chrome' : webdriver.Chrome,
    'firefox' : webdriver.Firefox,
    'edge' : webdriver.Edge,
    'opera' : webdriver.Opera,
    'safari' : webdriver.Safari,
    'android' : webdriver.Android,
}

receiver_mail = {
    'guozhengbao' : "4141847@qq.com",
    "zhangjunping" : "76656630@qq.com",
    "xieyuanzheng" : "121546683@qq.com",
    "liulianlong" : "368422559@qq.com",
    "liujianhua" : "181643605@qq.com",
    "lanronggui" : "297086499@qq.com",
    #测试部
    "wangwei" : "1015561002@qq.com",
    "huangjiaguo" : "1195375440@@.com",
    #产品部
    "xiaoguobin" : "369582902@qq.com",
    "zhouyuyin" : "353216405@qq.com",
    #开发部
    "yuewen" : "1324407659@qq.com",
    "guodongquan" : "648215166@qq.com",
    "maixuexi" : "1158447821@qq.com",
    "longwen" : "904235992@qq.com",
    "wangyajie" : "873589519@qq.com",
    "huangzihao" : "909695699@qq.com",
    "wuxin" : "1164554421@qq.com",
    "penghuihui" : "343239443@qq.com",
    "yanglin" : "781287462@qq.com",
    "dengjunjun" : "849302454@qq.com",
    "qihailiang" : "1607855394",
    "huzhuhua" : "834287041@qq.com"
}

receiver_mail_core = {
    'guozhengbao' : "4141847@qq.com",
    "zhangjunping" : "76656630@qq.com",
    "xieyuanzheng" : "121546683@qq.com",
    "liulianlong" : "368422559@qq.com",
    "liujianhua" : "181643605@qq.com",
    "lanronggui" : "297086499@qq.com",
}