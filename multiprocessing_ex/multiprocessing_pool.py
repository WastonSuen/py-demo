# coding=utf-8
"""
@version: 2018/2/22 022
@author: Suen
@contact: sunzh95@hotmail.com
@file: multiprocessing_pool
@time: 10:36
@note:  ??
"""

import time
from multiprocessing import Pool


def func(msg):
    for i in range(3):
        print(msg)
        time.sleep(1)
    return 'done <%s>' % msg


if __name__ == "__main__":
    pool = Pool(processes=4)
    result = []
    for i in range(10):
        msg = "hello %d" % (i)
        result.append(pool.apply_async(func, (msg,)))
    pool.close()
    pool.join()
    for res in result:
        print(res.get())
    print("Sub-process(es) done.")
