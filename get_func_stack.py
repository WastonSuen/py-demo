# coding=utf-8
"""
@version: 2018/1/31 031
@author: Suen
@contact: sunzh95@hotmail.com
@file: get_func_stack
@time: 17:26
@note:  ??
"""

import inspect
import functools


def func_caller_stack(func):
    """
    打印函数调用栈, 带参数的装饰器实现
    :return: 
    """

    @functools.wraps(func)
    def _func_caller_stack(*args, **kwargs):
        names = []
        frame = inspect.currentframe()
        ## Keep moving to next outer frame
        init_func = func.func_name
        init_filename = func.func_code.co_filename
        init_lineno = func.func_code.co_firstlineno
        names.append({'filename': init_filename, 'funcname': init_func, 'lineno': init_lineno})
        while True:
            try:
                frame = frame.f_back
                name = frame.f_code.co_name
                filename = frame.f_code.co_filename
                lineno = frame.f_lineno
                names.append({'filename': filename, 'funcname': name, 'lineno': lineno})
            except:
                break
        print('\n{} 函数调用栈:'.format(init_func))
        while True:
            try:
                index = names.pop()
                print('line:{:>4} >>> {:<25} {}'.format(index['lineno'], index['funcname'], index['filename']))
            except:
                break
        print('\n')
        ret = func(*args, **kwargs)
        return ret

    return _func_caller_stack
