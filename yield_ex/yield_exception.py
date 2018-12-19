# coding=utf-8
"""
@version: 2018/1/31 031
@author: Suen
@contact: sunzh95@hotmail.com
@file: yield_exception
@time: 14:59
@note:  ??
"""
import time


class MyException(Exception):
    pass


def raise_exc(n):
    for i in range(10):
        time.sleep(0.5)
        yield i
        if i == n:
            raise MyException('My Exception')


if __name__ == '__main__':
    f = raise_exc(2)
    next(f)
    while 1:
        try:
            print(next(f))
        # except StopIteration:
        #     print('catched: Stop')
        #     break
        except MyException as e:
            print('catched: %s' % e)
            break  # 如果此处不break, 则会继续调用next(f), 因生成器raise了异常, 所以生成器返回StopIteration, 被上一个异常catch
