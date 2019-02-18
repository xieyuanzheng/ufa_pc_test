import csv,os
from log.log import log1


def readall():
    # 读取csv的全部数据
    dir_curr = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    path = os.path.join(dir_curr,'login.csv')
    #path="D:\\Projects\\Python Project\\ufa_pc_test\\login.csv"
    csvfile = open(path,'r')
    readcsv = csv.reader(csvfile)
    print("------------")
    for row in readcsv:
        print(row)

def readrow():
    dir_curr = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    path = os.path.join(dir_curr,'login.csv')
    csvfile = open(path,'r')
    lines = csvfile.readlines()
    csvfile.close()
    row = [] #定义行数组
    column = [] #定义列数组
    for line in lines:
        row.append(line.split(','))
    row_num = row.__len__()
    for i in range(row_num):
        print(row[i])
    for col in row:
        column.append(col[0])
    print(column)

def readcolumn():
    dir_curr = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    path = os.path.join(dir_curr,'login.csv')
    csvfile = open(path,'r')
    lines = csvfile.readlines()
    csvfile.close()
    row = [] #定义行数组
    column = [] #定义列数组
    for line in lines:
        row.append(line.split(','))
    print(row)
    row_num = len(row)
    columm_num = len(row[0])
    print(row_num)
    print(columm_num)
    for i in range(columm_num):
        for col in row:
            column.append(col[i])
    print(column)
    print(column.__len__())



if __name__ == '__main__':
    try:
        log1.info("开始测试")
        r = 10/2
        log1.info(r)
    except ZeroDivisionError as e:
        log1.error("报错信息 : ",exc_info = 1)
    log1.info("end")