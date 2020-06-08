'''
str、tuple、set、dict、list 几种数据结构之间的转换
'''

# list、str

convert_list = [1, 2, 4, 'a', 'max']
str_list = str(convert_list)
print(str_list, type(str_list))
convert_str1 = 'string'
convert_str2 = 'This is string'
str_list1 = list(convert_str1)  # 讲一个字符串转化成一个列表
str_list2 = list(convert_str2)  # 将一个字符串转化成一个列表
str_list3 = convert_str2.split(' ')  # 讲一个字符串转化成一个列表，以空格为拆分
print(str_list1, str_list2, str_list3)  # ['s', 't', 'r', 'i', 'n', 'g'] ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 's', 't', 'r', 'i', 'n', 'g'] ['This', 'is', 'string']
