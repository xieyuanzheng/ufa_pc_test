import os


def getmemory():
    memory = os.popen("adb shell dumpsys meminfo")