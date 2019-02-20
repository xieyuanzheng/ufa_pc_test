import os


def getnetworkstatus():
    netstatus = os.popen("adb shell dumpsys netstats")


def getnetmanage():
    netman = os.popen("adb shell dumpsys network_management")