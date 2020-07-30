# python time calendar常用方法

'''
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00-59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''


import time, calendar


# 常用方法
def common_func():
    # 获取时间戳 从1970年开始
    print(time.time())

    # 获取当前时间
    print(time.localtime(time.time()))

# 格式化时间
def format_time():
    format_time1 = time.asctime(time.localtime(time.time()))   # asctime方法格式化时间
    # strftime格式化
    format_time2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    format_time3 = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

    # 格式化时间字符串转化为时间戳
    a = "Sat Mar 28 22:24:24 2016"
    b = time.time()
    time_stamp = time.mktime(b)


    print(format_time1, format_time2, format_time3, time_stamp)


# 计时
def timing():
    a = time.process_time()
    time.sleep(10)
    b = time.process_time()
    print(b-a)
    # time.perf_counter or time.process_time

def Calendar():
    aaa = calendar.monthlen(2020, 6)  # 月份多少天
    print(aaa)



if  __name__ == "__main__":
    common_func()
    # format_time()
    Calendar()
    timing()