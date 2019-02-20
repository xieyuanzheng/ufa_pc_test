import os


def getmemory():
    memory = os.popen("adb shell dumpsys meminfo")
    #VSS - Virtual Set Size 虚拟耗用内存
    #RSS - Resident Set Size 实际使用物理内存
    top = os.popen("adb shell top")
    #每秒刷新一次
    topfre = os.popen("adb shell top -d 1")