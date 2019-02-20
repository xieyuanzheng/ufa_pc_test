import os

def getlaunchtime():
    os.popen("adb shell am start -W -n com.ufa.scm/.mvp.splash.SplashActivity")

def coldstart():
    os.popen("adb shell am force-stop  com.ufa.scm")

def hotstart():
    os.popen("adb shell input keyevent 3")