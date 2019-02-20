import sys,os
import platform

# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)
#
# print("curPath : " + curPath)
# print("rootPath : " + rootPath)
print(sys.path)

from  pcui_testcase import path2

print(path2.isWindows())