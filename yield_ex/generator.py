# coding=utf-8
"""
@version: 2018/1/31 031
@author: Suen
@contact: sunzh95@hotmail.com
@file: generator
@time: 12:29
@note:  ??
"""

import time


def fib(n):
    a, b = 0, 1
    i = 0
    while i < n:
        yield b
        i += 1
        a, b = b, a + b


if __name__ == '__main__':
    for k in fib(20):
        print(k)
        time.sleep(1)
