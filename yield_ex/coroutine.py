# coding=utf-8
"""
@version: 2018/1/31 031
@author: Suen
@contact: sunzh95@hotmail.com
@file: coroutine
@time: 12:41
@note:  ??
"""

import time


def ping():
    print('ping 0')
    count = 1
    while 1:
        yield po  # 返回po
        print('ping ' + str(count))
        count += 1
        time.sleep(1)


def pong():
    print('pong 0')
    count = 1
    while 1:
        yield pipo  # 返回pipo
        print('pong ' + str(count))
        count += 1
        time.sleep(1)


def pingpong():
    print('pingpong 0')
    count = 1
    while 1:
        yield pi  # 返回pi
        print('pingpong ' + str(count))
        count += 1
        time.sleep(1)


def run(co):
    while 1:
        co = next(co)  # 通过调用next, co依次等于pi,po,pipo


if __name__ == '__main__':
    pi = ping()
    po = pong()
    pipo = pingpong()
    next(pi)
    next(po)
    next(pipo)
    run(pi)
