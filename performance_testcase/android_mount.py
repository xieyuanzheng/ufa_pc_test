import os


def getmount():
    mount = os.popen("adb shell dumpsys mount")