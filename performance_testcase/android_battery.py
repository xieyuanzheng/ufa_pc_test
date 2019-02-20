import os,re

def getbattery():
    #手机USB连接电脑后，会进入充电状态，要关闭之。
    #status = 2， 是充电状态，所以status非2即可
    #切换非充电状态 adb shell dumpsys battery set status 1
    battery = os.popen("adb shell dumpsys battery")
    matchObj = re.search(r'level: ([0-9]+)',battery.read())
    print(matchObj.group(1))

def getbatteryproperties():
    battery = os.popen("adb shell dumpsys batteryproperties")
    matchObj = re.search(r'level: ([0-9]+)',battery.read())
    print(matchObj.group(1))

def getbatterystate():
    battery = os.popen("adb shell dumpsys batterystate")
    matchObj = re.search(r'level: ([0-9]+)', battery.read())
    if matchObj:
        print(matchObj.group())