# coding=utf-8
"""
@version: 2018/2/9 009
@author: Suen
@contact: sunzh95@hotmail.com
@file: singleton
@time: 15:59
@note:  ??
"""


def singleton(cls):
    """
    use decorator
    :param cls: 
    :param args: 
    :param kwargs: 
    :return: 
    """
    ins = {}

    def _decorator(*args, **kwargs):
        if cls not in ins:
            ins[cls] = cls(*args, **kwargs)
        return ins[cls]

    return _decorator


def singleton_class(cls):
    ins = {}

    class _Decorator(cls):
        def __new__(cls, *args, **kwargs):
            if not cls in ins:
                ins[cls] = super(_Decorator, cls).__new__(cls)
            else:
                if not (sorted(ins[cls].args) == sorted(args) and ins[cls].kwargs == kwargs):
                    raise ValueError('单例模式每次实例化参数必须相同')
            return ins[cls]

    return _Decorator


@singleton_class
class SingletonClsWithDecorator(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def report(self):
        print(id(self), self.args, self.kwargs)


class SingletonClsWithNewKeyword(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)  # new关键字只传入cls, __new__ 负责返回实例, __init__ 才真正初始化
        else:
            if not (sorted(cls._instance.args) == sorted(args) and cls._instance.kwargs == kwargs):
                raise ValueError('单例模式每次实例化参数必须相同')
        return cls._instance

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def report(self):
        print(id(self), self.args, self.kwargs)


class Singleton(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_ins'):
            cls._ins = super(Singleton, cls).__call__(*args, **kwargs)
        else:
            if not (sorted(cls._ins.args) == sorted(args) and cls._ins.kwargs == kwargs):
                raise ValueError('单例模式每次实例化参数必须相同')
        return cls._ins


class SingletonClsWithMetaclass(metaclass=Singleton):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def report(self):
        print(id(self), self.args, self.kwargs)


if __name__ == '__main__':
    s1 = SingletonClsWithDecorator(1, 2, one=1, two=2)
    s2 = SingletonClsWithDecorator(1, 2, one=1, two=2)
    # s2 = SingletonClsWithDecorator(3, 4, three=3, four=4)
    s1.report()
    s2.report()
    print(s1 is s2)
    # 使用装饰器(singleton())的方法, 会使类变为函数, 为了将类保持, 可以将_decorator变为类(singleton_class())
    # 但会引入新的需要注意的点(与使用__new__关键字控制实例的问题一样)


    s1 = SingletonClsWithNewKeyword(1, 2, one=1, two=2)
    s2 = SingletonClsWithNewKeyword(1, 2, one=1, two=2)
    # s2 = SingletonClsWithNewKeyword(3, 4, three=3, four=4)
    # 第二次实例化该类, 会覆盖之前的实例, 并且会用新参数覆盖之前实例__init__的结果,
    # 这种情况需要根据需求来确定, 通常做法是不作处理, 让在本次运行环境中的单例可以更改,
    # 旧的实例会随着新实例化结果的改变而改变, 这里的代码为了方便理解, 做了限制相同参数的处理,
    # 所以加入了参数比较过程, 若参数不同引发异常。需特别注意这一点
    s1.report()
    s2.report()
    print(s1 is s2)

    s1 = SingletonClsWithMetaclass(1, 2, one=1, two=2)
    s2 = SingletonClsWithMetaclass(1, 2, one=1, two=2)
    # 第二次实例化该类, 会覆盖之前的实例, 并且会用新参数覆盖之前实例__init__的结果,
    # (与使用__new__关键字控制实例的问题一样)
    # 所以加入了参数比较过程, 若参数不同引发异常, 需特别注意这一点
    s1.report()
    s2.report()
    print(s1 is s2)
