'''
*args表示任何多个无名参数，它是一个tuple；**kwargs表示关键字参数，它是一个dict。并且同时使用*args和**kwargs时，
必须*args参数列要在**kwargs前，
像foo(a=1, b='2', c=3, a', 1, None, )这样调用的话，会提示语法错误“SyntaxError: non-keyword arg after keyword arg”。

'''

class ArgsKwargs():

    def useargs1(self, args):   # args不加*，只能传一个对象
        print(args)

    def useargs2(self, *args):  # args加*， 可以传入多个参数，返回一个tuple
        print(args)

    def userargs3(self, *args):
        print(*args)        # 打印*args, 打印tuple中的每个参数， **kwargs 不能这么打印

    def usekwargs(self, **kwargs):
        print(kwargs)

    def useargs_kwargs1(self, *args, **kwargs):
        print(args,kwargs)

    def useargs_kwargs2(self, *args, **kwargs):
        print('可以传入空值')




argskwargs = ArgsKwargs()
argskwargs.useargs1(1)
argskwargs.useargs2(1,3,'a')
argskwargs.usekwargs(a=1,b=2,c='c')
argskwargs.useargs_kwargs1(1,2,'a',d=1,e='e')
argskwargs.userargs3(1,2)
argskwargs.useargs_kwargs2()


'''
args在前,*kwargs在后面,也就是带等号的(字典格式)形参实参传入要放在后面
如果函数形参没有加*,那就是一个对象,如果加了*args,
表示可以传入多个实参进去,传入的参数被收集到一个元组args这个对象中,如果对这个元组对像使用*操作,表示解开,返回的是元组中的多个对象!
'''

