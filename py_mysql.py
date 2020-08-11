#python 连接mysql数据库并操作
# 多表联合操作
# https://blog.csdn.net/kongsuhongbaby/article/details/84948205

import pymysql

# 连接数据库
def py_mysql():
    # dbhost = '58.38.61.182'

    dbhost = '182.61.38.58'
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
    sql1 = "insert into Student values('test1','test1@qq.com', 28)"
    # 增加多条数据
    sql2 = "insert into Student values(%s, %s, %s)"

    # execute() 执行单条sql语句
    # cur.execute(sql1)
    # executemany() 执行多条sql语句，适用于批量插入
    cur.executemany(sql2, [('test2','test2@qq.com',21), ('test3','test3@qq.com',22),
                           ('test4','test4@qq.com',23), ('test5','test5@qq.com',24),
                           ('test6','test6@qq.com',25), ('test7','test7@qq.com',26)])
    db.commit()
    print("insert success")

def py_update(db):
    cur = db.cursor()
    update_sql = "update Student set age=22 where name='test2' or name='test4' or name='test6';"
    cur.execute(update_sql)
    cur.close()
    db.commit()

def py_delete(db):
    cur = db.cursor()
    delete_sql = "delete from Student where age=22;"
    cur.execute(delete_sql)
    cur.close()
    db.commit()

if __name__ == "__main__":
    db = py_mysql()
    # create_table(db=db)


    #sql1 = "insert into Student values('xiaoming','xiaoming@qq.com','22')"

    #execurte_sql(db, sql1)
    #db.commit()
    sql2 = "select * from Student where Name='xiaoming'"
    # select_result = execurte_sql(db, sql2)

    # print(select_result)
    # select_result = py_select(db)
    # print(select_result,type(select_result))
    # py_insert(db)
    # py_update(db)
    py_delete(db)