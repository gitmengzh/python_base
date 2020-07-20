'''
主要讲述一下os的常见方法
'''

import os

# 1 python在命令行中执行操作，os.popen()， os.system()
# Python调用Shell，有两种方法：os.system(cmd)或os.popen(cmd)脚本执行过程中的输出内容。实际使用时视需求情况而选择。
# os.system(cmd)的返回值是脚本的退出状态码，只会有0(成功),1,2
# os.popen(cmd)返回脚本执行的输出内容作为返回值

def py_shell():
    pop1 = os.popen("ping www.baidu.com")
    sys1 = os.system("ping www.baidu.com")
    print(pop1, 'aaa',  sys1)

# os.path
'''
os.path.abspath(path)  返回绝对路径
os.path.basename(path)	返回文件名
os.path.dirname(path)	返回文件所在的路径， c:/aaa/ccc.py  返回c:/aaa
os.path.readname(path)  如果文件通过链接进行关联，那么返回链接的目录
os.path.join(path1[, path2[, ...]])	把目录和文件名合成一个路径
'''
def os_path():
    abspath1 = os.path.abspath('.')  # 返回当前目录的绝对路径
    abspath2 = os.path.abspath('..') # 返回当前目录上一级目录的绝对路径
    basename = os.path.basename('c:/test/aaa/ccc.py') # 返回ccc.py
    path1 = 'aaa'
    path2 = 'bbb'
    path3 = 'ccc'
    path = os.path.join(path1,path2,path3) # 组成一个路径返回 aaa\bbb\ccc
    print(abspath1, abspath2, basename, path)


# os.renames(old, new) 递归地对目录进行更名，也可以对文件进行更名。
def os_reanmes(path1, path2):
    os.renames(path1, path2)

# os.listdir(path)  返回path指定的文件夹包含的文件或文件夹的名字的列表。
def os_listdir(path):
    path_list = os.listdir(path)
    print(path_list)

if __name__ == "__main__":
    path = 'C:/Users/meng4/Desktop/project/python/python_base/2'
    path2 = 'C:/Users/meng4/Desktop/project/python/python_base/3'
    #os_path()
    #os_listdir(path)
    #os_reanmes(path, path2)
    py_shell()