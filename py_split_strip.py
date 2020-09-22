'''
介绍strip和split相关方法使用
'''


# 删除字符串开头或者结尾的指定字符，默认为空格
def py_strip(s):
    s1 = s.strip()
    s2 = s.strip('a')
    s3 = s.strip('abcd') # 只要字符串前后只包含这个字符串中的内容，那么就去掉，例如ac结尾或者以ca结尾的
    return s3

# str.split(s) 以s对str进行分割，返回一个list
def py_split(s):
    result1 = s.split()
    result2 = s.split()
    result3 = s.split()
    result4 = s.split()
    result5 = s.split()








if __name__ == "__main__":
    str1 = 'abcd123ecb'
    str2 = 'abcd'
    str3 = ' ads '
    print(py_strip(str1))

