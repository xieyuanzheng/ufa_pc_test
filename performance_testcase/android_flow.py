import os

def gettraffic():
    #流量是指receive和transmit之和
    pro = os.popen("adb shell ps | findstr com.ufa.scm")
    #获取进程ID
    pid = pro.readlines()[0].split(" ")[5]
    ps = os.popen("adb shell cat /proc/" + pid +"/net/dev")