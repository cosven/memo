#-*- coding:utf8 -*-

'''
@note::
    帮助理解@pyqtSlot(int, str)
    下面也实现了函数参数检测

参考:
- U{http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html}

'''


def hello(arg1, arg2):     # arg1-int arg2-str
    print "hello:", arg1, arg2

    def _hello(func):   # func-foo
        def __hello(a, b):
            if type(a) == arg1 and type(b) == str:
                print "Ok, args are available"
                func(a, b)    #
            else:
                print "Please check the types of args"
        return __hello

    return _hello   # _hello(num)


@hello(int, str)
def foo(a, b):
    print "Foo:", a, b


'''
结果输出::
    >>> python decorator.py
    hello: <type 'int'> <type 'str'>
    Please check the types of args
    Ok, args are available
    Foo: 0 haha
'''

foo(3, 4)   # 调用两次foo，但是只会调用一次 外层hello函数
foo(0, "haha")
