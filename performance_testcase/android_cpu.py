import os

def getcpu():
    os.popen("adb shell dumpsys cpuinfo")


def getcpuByPackage():
    #看CPU值是否合理，要不断使用，看CPU使用率有没有继续上升，如果平稳，则没问题。最多不能超过85%
    os.popen("adb shell dumpsys cpuinfo | findstr com.ufa.scm")