import os

def getcpu():
    os.popen("adb shell dumpsys cpuinfo")


def getcpuByPackage():
    #��CPUֵ�Ƿ����Ҫ����ʹ�ã���CPUʹ������û�м������������ƽ�ȣ���û���⡣��಻�ܳ���85%
    os.popen("adb shell dumpsys cpuinfo | findstr com.ufa.scm")