import os


def getmemory():
    memory = os.popen("adb shell dumpsys meminfo")
    #VSS - Virtual Set Size ��������ڴ�
    #RSS - Resident Set Size ʵ��ʹ�������ڴ�
    top = os.popen("adb shell top")
    #ÿ��ˢ��һ��
    topfre = os.popen("adb shell top -d 1")