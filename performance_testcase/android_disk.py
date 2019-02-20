import re,os


def getdisk():
    disk = os.popen("adb shell dumpsys diskstats")