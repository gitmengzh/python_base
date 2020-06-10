# 主要介绍dict


dict1 = {'a':1, 'b':2, 'c': 3}
# 自定从python3.6输出开始变得有顺序
print(dict1.keys())  # dict_keys(['a', 'b', 'c'])
dict1.keys()  # 返回所有的key，返回类型不是list,但是可以遍历
dict1.values()  # 返回所有的value, 类型与keys类似
dict1.items()   # 返回所有的key value以元组的形式, 返回类型与keys类似
dict1.clear()   # 清空字典
dict1.get('b')  # 获取某个key的value
dict2 = {1:'a', 2:'b'}
dict1.update(dict2)# 将dict2 添加到dict1中
print(dict1)
