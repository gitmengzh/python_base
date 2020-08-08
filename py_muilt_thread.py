'''
python多线程
根据工作经历，需要用curl短时间并发大量请求
'''

import threading
import time
import os


def sing(num):
    for i in range(num):
        print("sing%d" % i)
        time.sleep(0.5)


def dance(num):
    for i in range(num):
        tmpres = os.popen('curl www.baidu.com').readlines()
        print(tmpres)



def main():
    """创建启动线程"""
    # t_sing = threading.Thread(target=sing, args=(5,))
    t_dance = threading.Thread(target=dance, args=(6, ))
    # t_sing.start()
    t_dance.start()


if __name__ == '__main__':
    main()


