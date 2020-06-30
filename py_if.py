'''
关于if
'''


#if...else...的简单实用
def if1():
    i = 10
    if i == 11:
        print('if条件成立')
    else:
        print('if 条件不成立，执行else')


# if...elif...else...的简单使用
def if2():
    i = 10
    if i < 1:
        print('if 条件成立')
    elif i >=10:
        print('elif 条件成立')
    else:
        print('if 和 elif条件都不成立')

# 单独if配合not使用
def if3():
    str1 = '222'
    list1 = []
    if not str1:  # str1不为空，所以not之后为false,条件不执行
        print('str1 为空')
        if not list1:
            print('list1 为空')



if __name__ == '__main__':
    if1()
    if2()
    if3()