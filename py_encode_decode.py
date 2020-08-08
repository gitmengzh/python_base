
'''
encode()  unicode(python3的str类型) 编码 -> gbk、utf-8(python3的bytes类型)
decode() 以指定的编码格式解码bytes对象，默认是utf-8,  gbk、utf-8(python3的bytes类型) 解码 ->unicode(python3的str类型)
str类型： 表示字符串，Unicode
bytes类型： 表示二进制数据

python3 在默认情况下，以utf-8将程序存储在硬盘中， 解释器以utf-8去取程序
如果一个文件以gbk编码存储，你用utf-8的编码格式去读取，那么读出来为乱码




'''
a = "你好"
print(a.encode())
b = b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(b.decode())
print(a.encode(encoding='gbk'))
