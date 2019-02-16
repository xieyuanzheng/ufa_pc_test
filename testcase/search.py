import unittest,os,time,logging
from config.config_01 import broswer_config
from constant.constant_01 import UFA_HOME_URL


class GoodsSearch(unittest.TestCase):
    u"""商品搜索"""
    chrome_driver = 'F:\\tools\\chromedriver.exe'
    browser = broswer_config['chrome'](executable_path=chrome_driver)

    def test_s1_goodssearch(self):
        u"""未登录不能查看价格"""
        self.browser.get(UFA_HOME_URL)
        self.browser.maximize_window()
        isFlag = True
        current_handle = self.browser.current_window_handle
        logging.info("-----logging---------")
        #输入搜索商品
        self.browser.find_element_by_xpath("/html/body/header/div[2]/div[2]/div[2]/span/input[1]").send_keys("白蜡木")
        self.browser.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        #判断：未登录不可查看价格
        tip = self.browser.find_element_by_xpath('/html/body/div/div/ul/li[1]/a/div[2]/em[1]').text
        if not tip == "登录后查看价格":
            isFlag = False
        self.assertEqual(True,isFlag)
        self.browser.quit()


class StoreSearch(unittest.TestCase):
    u"""店铺搜索"""
    chrome_driver = 'F:\\tools\\chromedriver.exe'
    browser = broswer_config['chrome'](executable_path=chrome_driver)

    def test_s1_storesearch(self):
        u"""搜索-东莞众家联供应链服务有限公司"""
        self.browser.get(UFA_HOME_URL)
        self.browser.maximize_window()
        isFlag = True
        current_handle = self.browser.current_window_handle
        #点击店铺全搜索
        self.browser.find_element_by_xpath('/html/body/header/div[2]/div[2]/div[1]/span[2]').click()
        self.browser.find_element_by_xpath('//*[@id="search"]').click()
        store_name_first = self.browser.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div[1]/div[1]/b/a').text
        time.sleep(5)
        if store_name_first == "":
            isFlag = False
        #定点搜索
        self.browser.find_element_by_xpath('/html/body/header/div[2]/div[2]/div[2]/span/input[1]').send_keys("东莞众家联供应链服务有限公司")
        self.browser.find_element_by_xpath('//*[@id="search"]').click()
        store_name_search = self.browser.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div[1]/div[1]/b/a').text
        if store_name_search != "东莞众家联供应链服务有限公司":
            isFlag = False
        #打开店铺首页
        self.browser.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div[1]/div[1]/b/a').click()
        handles = self.browser.window_handles
        for handel in handles:
            if handel != current_handle:
                self.browser.switch_to_window(handel)
                title = self.browser.title
                if title != "东莞众家联供应链服务有限公司":
                    isFlag = False
        self.assertEqual(True,isFlag)
        self.browser.quit()