import time,os


def MakeReport(filename):
    fp = open(filename, 'wb')
    return fp

def getFilename():
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    dir1 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    dir2 = os.path.join(dir1, 'log')
    filename = os.path.join(dir2, "report" + now + "result.html")