import os
from log.log import log1

#os.system("ipconfig")
log1.warn("-----------")
#print(os.system("ipconfig"))
p = os.popen("ipconfig")
print(p.read())

os.system("adb shell dumpsys meminfo  com.ufa.scm")