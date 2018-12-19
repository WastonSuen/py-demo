# coding=utf-8
"""
@version: 2017/11/22 022
@author: Suen
@contact: sunzh95@hotmail.com
@file: clockdeco
@time: 11:42
@note:  ??
"""
#

import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        result = func(*args, **kwargs)
        arg_str = ', '.join(arg_lst)
        elapsed = time.time() - t0
        name = func.__name__
        print('[%0.8fs] %s(%s) -> %s ' % (elapsed, name, arg_str, result))
        return result

    return clocked
