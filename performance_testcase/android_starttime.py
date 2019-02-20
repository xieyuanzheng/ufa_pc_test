import os

def getlaunchtime():
    #ÀäÈÈÆô¶¯£¬Æô¶¯ÃüÁî
    os.popen("adb shell am start -W -n com.ufa.scm/.mvp.splash.SplashActivity")

def coldstart():
    #ÀäÆô¶¯£¬Í£Ö¹ÃüÁî
    os.popen("adb shell am force-stop  com.ufa.scm")

def hotstart():
    #ÈÈÆô¶¯£¬Í£Ö¹ÃüÁî
    os.popen("adb shell input keyevent 3")