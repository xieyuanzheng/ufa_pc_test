from selenium import webdriver
import time


# 常量部分（固定不变使用频繁的参数维护在此处）
UFA_HOME_URL = 'https://www.ufa.hk'
UFA_MALL_URL = 'https://www.ufa.hk/mall/index.html'
UFA_LOGIN_URL = 'https://www.ufa.hk/mall/login.html'
UFA_LOGIN_ADMIN = 'https://www.ufa.hk/admin/'

DB_Mysql = {
    "HOST" : "localhost",
    "USER" : "jamko",
    "PASSWORD" : "ufa123456",
    "NAME" : "interfacetestcase",
    "CHARSET":"utf8"
}