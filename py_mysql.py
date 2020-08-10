#python 连接mysql数据库并操作

import pymysql

# 连接数据库
def py_mysql():
    dbhost = '58.38.61.182'

    dbuser = 'root'
    dbpwd = '!Wangbingxu1'
    dbname = 'py_test1'
    try:
        db = pymysql.connect(dbhost, dbuser, dbpwd, dbname)
        # print('数据库连接成功!')
        return db
    except pymysql.Error as e:
        print('数据库连接失败' + str(e))

def execurte_sql(db, sql):
    cur = db.cursor()
    cur.execute(sql)




def create_table(db):
    cur = db.cursor()
    cur.execute('DROP TABLE IF EXISTS new_table')
    # sqlQuery = "CREATE TABLE Student(Name CHAR(20) NOT NULL ,Email CHAR(20),Age int )"
    # cur.execute(sqlQuery)
    print('create table success')


if __name__ == "__main__":
    db = py_mysql()
    # create_table(db=db)


    #sql1 = "insert into Student values('xiaoming','xiaoming@qq.com','22')"

    #execurte_sql(db, sql1)
    #db.commit()
    sql2 = "select * from Student where Name='xiaoming'"
    select_result = execurte_sql(db, sql2)
    print(select_result)