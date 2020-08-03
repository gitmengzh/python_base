# python 中json的序列化
import json


'''
json 语法:

    数据在名称/值对中
    数据由逗号分隔
    花括号保存对象, 
    方括号保存数组
    
    JSON 值可以是：

    数字（整数或浮点数）
    字符串（在双引号中）
    逻辑值（true 或 false）
    数组（在方括号中）
    对象（在花括号中）
    null
    对象和数组的使用区别

'''
json1 = [ {'aaa', 'bbb', 'ccc'},
          {'111', '222', '333'},
          {'abc', '123'},
          ]
json2 = {'student': [{'name': 'jone', 'age': 20},
                     {'name': 'hank', 'age': 21},
                    {'name': 'lily', 'age': 20}]}
json3 = {'name':'tom', 'age': 18}
json4 = [{'name':'tom'}]


'''
python 中关于json解析的方法：
dumps()  将python对象编码成json字符串
loads()  将json字符串解码为python对象
dump()   将python内置类型编码成json字符串并写入文件
load()   读取文件中的json并解码成python对象
'''

