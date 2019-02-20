import os,re


def getdevices():
    devices = os.popen("adb devices")
    #print(devices.read())
    #result = re.match("\w+",devices.read())
    #print(result)
    #line = "List of devices attached I7EUIJORE6YTKVR8	device"
    matchObj = re.search(r'(\w{5,})\s+device', devices.read())
    print(matchObj.group(1))

def getpackages():
    packages = os.popen("adb shell pm list packages")
    matchObj = re.search(r'package:com.ufa.scm',packages.read())
    print(matchObj.group(0))


if __name__ == "__main__":
    counter = 10
    while counter>0:
        getdevices()
        print(counter)
        counter -= 1