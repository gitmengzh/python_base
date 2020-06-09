'''
list 常规操作和常用方法

'''

list1 = [1,2,3,'a','b']


# 新建列表



# 更新列表

list_update = ['a', 'c', '1', 2]
list_update.append(3)
print(list_update)

# 删除列表
list_del = [1, 3, 5, 'a']
del list_del[1]
print(list_del, '删除第二个元素')

# 列表操作符
# 两个列表可以直接相加得到新的列表
print(list_update+list_del, '合并两个数组')

# 得到一个全是重复元素的列表
print(['a']*10, '创建元素相同的列表')

# 切片操作
# a[:]           # a copy of the whole array
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[start:stop]  # items start through stop-1
# a[start:stop:step] # start through not past stop, by step

sample_list1 = [1, 3, 4, 5, 7, '2', 'a']
copy_list1 = sample_list1[:]
print(copy_list1, '利用切片复制列表' )
print(sample_list1[-1], '利用切片打印最后一个元素')
print(sample_list1[::-1], '利用切片反转列表')
print(sample_list1[1:3], '利用切片打印第二第三个元素')
print(sample_list1[1::2], '利用切片，从2个元素开始打印，步幅为2')
print(sample_list1[-2:], '利用切片，从倒数第二个元素开始打印到最后')
print(sample_list1[2::-2],'利用切片，从索引为2的元素开始，逆序到最后，步幅为2')


'''
内置方法
list.append(元素) # 以列表形式追加元素
list.clear() # 清空列表
list.copy() # 拷贝列表（新变量）
list.count() # 统计元素出现的次数
list.extend(元素) # 以迭代方式追加元素
list.index() # 返回元素索引位置
list.insert(索引) # 指定位置插入元素
list.pop(索引) #  删除指定位置的元素并返回元素
list.remove(元素) # 删除指定元素
list.reverse() # 反转元素
list.sort() # 排序
'''



