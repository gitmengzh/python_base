# python sys.path
'''
sys.path   sys.path是一个python搜索模块的路径列表
常用方法，append  增加模块导入路径
'''
import sys,os

path1 = os.path.abspath('..')

sys.path.append(path1+'/test_file')
path2 = os.path.dirname(path1)+'/test_file'
# aaa = os.listdir(path2)
print(sys.path[0])
#
# with open(path2+'/1.txt', 'r') as r:
#     aaa = r.read()
#     print(aaa)



