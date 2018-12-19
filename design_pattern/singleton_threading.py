# coding=utf-8
"""
@version: 2018/2/11 011
@author: Suen
@contact: sunzh95@hotmail.com
@file: singleton_threading
@time: 14:34
@note:  ??
"""

import time
import threading


class SingletonClsWithNewKeyword(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            time.sleep(1)
            cls._instance = super().__new__(cls)  # new关键字只传入cls, 其他参数会自动传入
        else:
            if not (sorted(cls._instance.args) == sorted(args) and cls._instance.kwargs == kwargs):
                raise ValueError('单例模式每次实例化参数必须相同')
        return cls._instance

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def report(self):
        print(id(self), self.args, self.kwargs)


def task(arg):
    obj = SingletonClsWithNewKeyword()
    print(id(obj))


class SingletonClsWithNewKeywordThreading(object):
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not hasattr(cls, '_instance'):
                time.sleep(1)
                cls._instance = super().__new__(cls)  # new关键字只传入cls, 其他参数会自动传入
            else:
                if not (sorted(cls._instance.args) == sorted(args) and cls._instance.kwargs == kwargs):
                    raise ValueError('单例模式每次实例化参数必须相同')
        return cls._instance

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def report(self):
        print(id(self), self.args, self.kwargs)


def task_threading(arg):
    obj = SingletonClsWithNewKeywordThreading()
    print(id(obj))


if __name__ == '__main__':
    # 会产生不同id的实例, 说明单例模式出现了bug, 多线程模式下, 未加锁会导致线程不安全
    print('No threading lock:\n')
    for i in range(10):
        t = threading.Thread(target=task, args=[i, ])
        t.start()

    # 加入线程锁
    print('With threading lock:\n')
    for i in range(10):
        t = threading.Thread(target=task_threading, args=[i, ])
        t.start()
