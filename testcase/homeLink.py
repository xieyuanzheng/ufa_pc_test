import unittest,os,time
from config.config_01 import broswer_config
from constant.constant_01 import UFA_HOME_URL
from log.log import log1


class HomeLinkAndDetailSD(unittest.TestCase):
    u"""供求市场"""
    chrome_driver = 'F:\\tools\\chromedriver.exe'
    browser = broswer_config['chrome'](executable_path=chrome_driver)

    def test_s1_supplyAndDemand(self):
        u"""供求列表及详情页"""
        self.browser.get(UFA_HOME_URL)
        self.browser.maximize_window()
        first_handle = self.browser.current_window_handle # 当前窗口句柄
        isFlag = True
        #self.browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/a[2]').click()
        self.browser.find_element_by_xpath('//a[@href="https://www.ufa.hk/demand/list.html"]').click()
        handles = self.browser.window_handles  # 获取当前窗口句柄集合（列表类型）
        time.sleep(3)
        for handle in handles:
            if handle != first_handle:
                #转换到供求列表页
                self.browser.switch_to_window(handle)
                #判断供求列表是否为空
                sd_type = self.browser.find_element_by_xpath("/html/body/div[4]/div[1]/ul/li[1]/span[1]").text
                if not (sd_type == "供应" or sd_type == "采购"):
                    log1.info(sd_type)
                    isFlag = False
                    #如果出错就截屏
                    now = time.strftime("%Y-%m-%d-%H-%M", time.localtime(time.time()))
                    current_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
                    save_dir = os.path.join(current_dir, "screenshot")
                    self.browser.save_screenshot(os.path.join(save_dir, now + ".jpg"))
                else:
                    log1.info("else : " + str(sd_type))
                    self.browser.find_element_by_xpath('/html/body/div[4]/div[1]/ul/li[1]/span[11]/a').click()
                    current_handle1 = self.browser.current_window_handle
                    if current_handle1 != handle:
                        self.browser.switch_to_window(current_handle1)
                        public_name = self.browser.find_element_by_xpath('//*[@id="publishUserName"]').text
                        if public_name == "":
                            isFlag = False
        self.assertEqual(True,isFlag)
        self.browser.quit()

class HomeLinkAndDetailInfo(unittest.TestCase):
    u"""行情资讯"""
    chrome_driver = 'F:\\tools\\chromedriver.exe'
    browser = broswer_config['chrome'](executable_path=chrome_driver)

    def test_s2_information(self):
        u"""行情资讯及详情页"""
        self.browser.get(UFA_HOME_URL)
        self.browser.maximize_window()
        isFlag = True
        current_handle = self.browser.current_window_handle
        #打开资讯列表页
        self.browser.find_element_by_xpath('//a[@href="https://www.ufa.hk/info.html"]').click()
        time.sleep(2)
        handles = self.browser.window_handles
        for handle in handles:
            if handle != current_handle:
                self.browser.switch_to_window(handle) #转换到资讯列表页
                info_title = self.browser.title
                if not info_title == "行情资讯":
                    isFlag = False
                time.sleep(5)
                subtitle1 = self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[1]/h3/span[1]').text
                subtitle2 = self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/h3/span[1]').text
                subtitle3 = self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[3]/div[1]/h3/span[1]').text
                subtitle4 = self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[4]/div[1]/h3/span[1]').text
                # if not subtitle1=="专题报道" or subtitle2=="新闻资讯" or subtitle3=="独家观点" or subtitle4=="展会资讯":
                #     isFlag = False
                if not subtitle1=="专题报道" and subtitle2=="新闻资讯" and subtitle3=="独家观点" and subtitle4=="展会资讯":
                    isFlag = False
        self.assertEqual(True,isFlag)
        self.browser.quit()

class HomeLinkAndDetailVideo(unittest.TestCase):
    u"""精彩视频"""
    chrome_driver = 'F:\\tools\\chromedriver.exe'
    browser = broswer_config['chrome'](executable_path=chrome_driver)

    def test_s3_video(self):
        u"""精彩视频及详情页"""
        self.browser.get(UFA_HOME_URL)
        self.browser.maximize_window()
        current_handle = self.browser.current_window_handle
        isFlag = True
        # 打开精彩视频列表页
        self.browser.find_element_by_xpath('//a[@href="https://www.ufa.hk/portal/video/list.html"]').click()
        handles = self.browser.window_handles
        for handle in handles:
            if handle != current_handle:
                self.browser.switch_to_window(handle)
                video_title = self.browser.title
                if not video_title == "视频播放":
                    isFlag = False
        self.assertEqual(True,isFlag)
        self.browser.quit()
