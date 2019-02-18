import pymysql
from constant import constant_01


#操作mysql数据库
def fetchone_mysql(sql):
    # 操作数据库
    #db = pymysql.Connect(host="localhost", user="jamko", passwd="ufa123456", db="interfacetestcase", charset="utf8")
    db = pymysql.Connect(host=constant_01.DB_Mysql["HOST"], user=constant_01.DB_Mysql["USER"], passwd=constant_01.DB_Mysql["PASSWORD"],
                         db=constant_01.DB_Mysql["NAME"], charset=constant_01.DB_Mysql["CHARSET"])
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    #print("DataBase version is : %s" % data)
    #cursor.execute("SELECT * from interfacetestcase.author")
    cursor.execute(sql)
    data2 = cursor.fetchone()
    #print("author is : %s" % data2[3])
    cursor.close()
    db.close()
    return data2

def fetchall_mysql(sql):
    # 操作数据库
    db = pymysql.Connect(host=constant_01.DB_Mysql["HOST"], user=constant_01.DB_Mysql["USER"],passwd=constant_01.DB_Mysql["PASSWORD"],
                         db=constant_01.DB_Mysql["NAME"], charset=constant_01.DB_Mysql["CHARSET"])
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    #print("DataBase version is : %s" % data)
    #cursor.execute("SELECT * from interfacetestcase.author")
    cursor.execute(sql)
    data2 = cursor.fetchall()
    #print("author is : %s" % data2[3])
    cursor.close()
    db.close()
    return data2

def insert_mysql(sql):
    db = pymysql.Connect(host=constant_01.DB_Mysql["HOST"], user=constant_01.DB_Mysql["USER"],
                         passwd=constant_01.DB_Mysql["PASSWORD"],
                         db=constant_01.DB_Mysql["NAME"], charset=constant_01.DB_Mysql["CHARSET"])
    cursor = db.cursor()
    result = cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    return result

def update_mysql(sql):
    db = pymysql.Connect(host=constant_01.DB_Mysql["HOST"], user=constant_01.DB_Mysql["USER"],
                         passwd=constant_01.DB_Mysql["PASSWORD"],
                         db=constant_01.DB_Mysql["NAME"], charset=constant_01.DB_Mysql["CHARSET"])
    cursor = db.cursor()
    result = cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    return result

def delete_mysql(sql):
    db = pymysql.Connect(host=constant_01.DB_Mysql["HOST"], user=constant_01.DB_Mysql["USER"],
                         passwd=constant_01.DB_Mysql["PASSWORD"],
                         db=constant_01.DB_Mysql["NAME"], charset=constant_01.DB_Mysql["CHARSET"])
    cursor = db.cursor()
    result = cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    return result