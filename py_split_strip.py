'''
介绍strip和split相关方法使用
'''


# 删除字符串开头或者结尾的指定字符，默认为空格
def py_strip(s):
    s1 = s.strip()
    s2 = s.strip('a')
    s3 = s.strip('abcd')  # 只要字符串前后只包含这个字符串中的内容，那么就去掉，例如ac结尾或者以ca结尾的
    return s3

# str.split(s) 以s对str进行分割，返回一个list
def py_split(s):
    result1 = s.split()  # 按照空字符进行分割,返回一个list
    result2 = s.split('s')  # 以s进行分割
    result3 = s.split('s', 2)  # 分割成两次，分成三段
    return result3



if __name__ == "__main__":
    str1 = 'abcd123ecb'
    str2 = 'abcd'
    str3 = ' ads '
    split_str1 = ' sdf dsfe sdffd '
    split_str2 = 'asdscsgsa'
    split_str3 = 'asdscs'    # 如果字符串末尾正好是分割字符，那么最终在返回的列表中会有个空值

    # print(py_strip(str1))
    print(py_split(split_str2))


