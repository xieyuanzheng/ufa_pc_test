import os,re


def getmonitor():
    monitor = os.popen("adb shell dumpsys devicestoragemonitor")