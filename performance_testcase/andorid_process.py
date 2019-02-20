import os


def getprocess():
    process = os.popen("adb shell dumpsys processinfo")


def getprocstats():
    procstats = os.popen("adb shell dumpsys procstats")