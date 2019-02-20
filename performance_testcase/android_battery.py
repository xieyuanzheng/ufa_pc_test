import os,re

def getbattery():
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