#python 连接mysql数据库并操作
# 多表联合操作
# https://blog.csdn.net/kongsuhongbaby/article/details/84948205

import pymysql

# 连接数据库
def py_mysql():
    # dbhost = '58.38.61.182'

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

def py_select(db):
    cur = db.cursor()
    sql2= "select * from Student where name='aaas';"
    cur.execute(sql2)

    # 三个函数返回tuple类型，
    result1 = cur.fetchone()     # 返回单行数据，如果没有，返回None
    result2 = cur.fetchmany(2)   # 返回指定行数的数据，如果没有，返回(),类型NoneType
    result3 = cur.fetchall()     # 返回所有数据，如果没有，返回（），tuple类型
    return result3

def py_insert(db):
    cur = db.cursor()
    # 增加单条数据
    sql1 = "insert into Student('test1','test1@qq.com', 28)"
    # 增加多条数据
    sql2 = ""
def py_update(db):
    pass

def py_delete(db):
    pass

if __name__ == "__main__":
    db = py_mysql()
    # create_table(db=db)


    #sql1 = "insert into Student values('xiaoming','xiaoming@qq.com','22')"

    #execurte_sql(db, sql1)
    #db.commit()
    sql2 = "select * from Student where Name='xiaoming'"
    # select_result = execurte_sql(db, sql2)

    # print(select_result)
    select_result = py_select(db)
    print(select_result,type(select_result))