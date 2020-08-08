#python 连接mysql数据库并操作

import pymysql

def py_mysql():
    dbhost = '58.38.61.182'
    dbuser = 'root'
    dbpwd = '!Wangbingxu1'
    dbname = 'py_test1'
    try:
        db = pymysql.connect(dbhost, dbuser, dbpwd, dbname)
        print('数据库连接成功!')
        return db
    except pymysql.Error as e:
        print('数据库连接失败' + str(e))


def create_table(db):
    cur = db.cursor()
    cur.execute('DROP TABLE IF EXISTS Student')
    sqlQuery = "CREATE TABLE Student(Name CHAR(20) NOT NULL ,Email CHAR(20),Age int )"
    cur.execute(sqlQuery)


if __name__ == "__main__":
    create_table(py_mysql())