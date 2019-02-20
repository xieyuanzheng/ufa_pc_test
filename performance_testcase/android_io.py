import os


def getio():
    io = os.popen("adb shell dumpsys ioinfo")