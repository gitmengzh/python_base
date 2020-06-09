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


# list 转 str
convert_list2 = ['1', '2', 'a', 'hello']
convert_str3 = ''.join(convert_list2)
print(convert_str3)  # 输出 12ahello， 必须保证list中全部都是字符格式的元素



# list&tuple list和tuple互相转换直接强制转化
list_tuple1 = (1,2,'a')
tuple_list1 = [22,'a']
print(list(list_tuple1), tuple(tuple_list1))

'''
复习一下list和tuple的区别，list 有序 可变，tuple 有序、不可变

如何让tuple可变呢，在tuple中嵌套list（或者其他可变数据结构），改变list
'''



L = {'p':'P','y':'Y','t':'T','h':'H','o':'O','n':'N'}
print('_'.join(L.values()))
