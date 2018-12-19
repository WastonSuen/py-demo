# coding=utf-8
"""
@version: 2018/2/23 023
@author: Suen
@contact: sunzh95@hotmail.com
@file: multiprocessing_manager
@time: 13:57
@note:进程间通信方式: Pipe, Queue都只在同一个父进程下使用, 若是pool, 则使用Manager
"""

import time
from multiprocessing import Manager, Pool


def queue_put(msg, queue):
    print('put %s' % msg)
    queue.put(msg)
    time.sleep(1)


if __name__ == '__main__':
    manager = Manager()
    queue = manager.Queue()
    pool = Pool(4)
    result = []
    for i in range(10):
        result.append(pool.apply_async(queue_put, args=('number: %s' % i, queue)))
    pool.close()
    pool.join()
    for i in range(queue.qsize()):
        print('get %s' % queue.get())
