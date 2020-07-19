'''
读写文件


mode常用的模式：

r：表示文件只能读取
w：表示文件只能写入
a：表示打开文件，在原有内容的基础上追加内容，在末尾写入
w+:表示可以对文件进行读写双重操作
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

def write_txt_file1(path):
    with open(path, 'w') as f4:
        content4 = f4.write('111')
        print(type(content4))


def write_txt_file2(path):
    with open(path, 'a') as f5:
        content6 = f5.write('aaaa')
        print(content6)

#
def read_write_txt_file(path):
    with open(path, 'w+') as f6:
        content7 = f6.read()
        # f6.write('66666')

        print(content7)


def wr_test():
    f = open('C:/Users/meng4/Desktop/project/testfile/1.txt', 'r+')
    # f.write('sss123')
    content = f.read()
    print(content)
    f.close()


if __name__ == "__main__":
       file_path ='C:/Users/meng4/Desktop/project/testfile/1.txt'
       # read_txt_file(file_path)
       # read_txt_file3(file_path)
       # write_txt_file2(file_path)
       read_write_txt_file(file_path)

       # wr_test()
