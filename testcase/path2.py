import sys,os
import platform


def isWindows():
    if 'Windows' in platform.system():
        print("it is windows platform!")
    else:
        print("it is not windows platforms.")