import os

def gettraffic():
    #������ָreceive��transmit֮��
    pro = os.popen("adb shell ps | findstr com.ufa.scm")
    #��ȡ����ID
    pid = pro.readlines()[0].split(" ")[5]
    ps = os.popen("adb shell cat /proc/" + pid +"/net/dev")