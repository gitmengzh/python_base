'''
读写文件


mode常用的模式：

r：表示文件只能读取
w：表示文件只能写入
a：表示打开文件，在原有内容的基础上追加内容，在末尾写入

r+:
a+:
mode参数可以省略不填，默认为r模式mode参数还可以指定以什么样的编码方式读写文本，默认情况下open是以文本形式打开文件的，比如上面的四种mode模式。

当你需要以字节（二进制）形式读写文件时，只需要在mode参数中追加'b'即可：

rb：以二进制格式打开一个文件，用于只读
wb：以二进制格式打开一个文件，用于只写
ab：以二进制格式打开一个文件，用于追加
wb+:以二进制格式打开一个文件，用于读写
'''

# read
def read_txt_file(path):
    with open(path, 'r') as f1:
        content1 = f1.read()
        print(content1)

# readlines方法输出为数组，每一行为一个数组的元素
def read_txt_file2(path):
    with open(path, 'r') as f2:
        content2 = f2.readlines()
        for i in content2:
            print(i)


# readline 每次读取一行，包括换行符，后一个readline会从上一个readline读取的位置继续读取
def read_txt_file3(path):
    with open(path, 'r') as f3:
        content3_1 = f3.readline()
        content3_2 = f3.readline()
        print(content3_1, content3_2)
# w mode， 重新写入内容
def write_txt_file1(path):
    with open(path, 'w') as f4:
        content4 = f4.write('111') # 返回为写入内容字符长度
        print(content4)

# a mode, 追加内容
def write_txt_file2(path):
    with open(path, 'a') as f5:
        content6 = f5.write('aaaa')
        print(content6)

#a+ mode: 在后一行添加内容，指针一直在文件最后，想要读取内容，需要用seek
#如果找不到该文件会在相应的路径下创建新文件
def a_plus_mode(path):
    with open(path, 'a+') as f6:
        # f6.seek(0)
        # content = f6.read()
        f6.write('12345')
        f6.seek(0)
        content7 = f6.read()
        print(content7,'###')
        f6.close()

# w+ mode:试验结果，先对文件进行写操作，无论有没有write方法，都会清空内容（可以理解完全覆盖）
# 如果找不到文件，会在路径中创建相应文件
# 想要读取全部内容，也必须用seek方法将指针指到开始位置
def w_plus_mode(path):
    with open(path, 'w+') as f:
        f.write('ssss')
        f.seek(0)
        content = f.read()
        print(content)
        f.close()

# r+ mode, 1 如果先read,再write,那么read读取的为原来内容
# 2 先write，再read，write将会替换掉相应个数的字符，read只能读取没有被替换的剩余字符 ，例如原值‘aaaa', write’vv'，则read内容为‘aa'
# 第二种情况是因为read的指针是被替换之后的指针地址，如果想要获取写后的内容，通过seek方法，从初始地址开始读即可
# 不能创建新文件，如果找不到改文件报错
def r_plus_mode(path):
    with open(path, 'r+') as f:
        # content1 = f.read()
        f.write('33')
        f.seek(0)
        content2 = f.read()
        print('###',content2)
        f.close()



if __name__ == "__main__":
       file_path ='C:/Users/meng4/Desktop/project/testfile/4.txt'
       # read_txt_file(file_path)
       # read_txt_file3(file_path)
       # write_txt_file2(file_path)
       # read_write_txt_file(file_path)
       # r_plus_mode(file_path)
       # w_plus_mode(file_path)
       a_plus_mode(file_path)
