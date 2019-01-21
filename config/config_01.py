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