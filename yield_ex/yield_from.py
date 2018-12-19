# coding=utf-8
"""
@version: 2018/1/31 031
@author: Suen
@contact: sunzh95@hotmail.com
@file: yield_from
@time: 14:34
@note: flatten, 使用 yield_from 展开多层列表。

yield from x, 作用相当于 for xx in x: yield xx, 且无需自己处理StopIteration异常
"""

from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)  # 这里递归调用，如果x是可迭代对象，继续分解
        else:
            yield x


if __name__ == '__main__':
    items = [1, 2, [3, 4, [5, 6], 7], 8]
    # Produces 1 2 3 4 5 6 7 8
    for x in flatten(items):
        print(x)
