'''
这是一个练习python装饰器的文件
面向切面编程。
应用场景比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
@符号是装饰器的糖语法

个人理解，当一个函数被很多不同的函数调用，那么就可以使用装饰器来接解决代码重复的问题
比如下面的例子，定义一个装饰器为user_logging
foo函数和bar函数可以被这个装饰器装饰，然后产生log
'''


# 装饰器

import logging
def user_logging(func):

    def wrapper(*args, **kwargs):
        logging.warning("%s is running" % func.__name__)
        return func(*args)
    return wrapper

@user_logging
def foo():
    print("i am foo")

@user_logging
def bar():
    print("i am bar")

bar()









# yield  迭代器    生成器

# def test_yield(i):
#
#     res = yield i+1
#
#
# g  = test_yield(5)
# print(next(g))
