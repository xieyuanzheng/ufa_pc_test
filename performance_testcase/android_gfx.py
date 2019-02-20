import os


def getgfx():
    gfx = os.popen("adb shell dumpsys gfxinfo")