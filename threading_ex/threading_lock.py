# coding=utf-8
"""
@version: 2017/12/13 013
@author: Suen
@contact: sunzh95@hotmail.com
@file: threading_lock
@time: 11:58
@note:  Lock, 全局锁; Rlock:线程锁, 递归锁
"""
#

import random
import threading
import time

mylock = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self, i):
        super(MyThread, self).__init__()
        self.i = i

    def run(self):
        global share
        for j in range(3):
            mylock.acquire()
            print(share, )
            share += self.i
            time.sleep(random.random())
            print("+ {} = {}".format(self.i, share))
            mylock.release()


if __name__ == '__main__':
    share = 10
    td1 = MyThread(1)
    td2 = MyThread(2)
    td1.start()
    td2.start()
