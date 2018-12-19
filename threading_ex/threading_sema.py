# coding=utf-8
"""
@version: 2017/12/13 013
@author: Suen
@contact: sunzh95@hotmail.com
@file: threading_sema
@time: 13:17
@note:  可用作连接池, 连接数被占满时调用acquire将阻塞
"""
#
import random
import threading, time

share_sema = threading.Semaphore(2)


class MyThread(threading.Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        global share
        if share_sema.acquire():
            print("{} Got Resource share: {}".format(self.name, share))
            share += 1
            time.sleep(random.random()*10)
        print("{} Release Resource share: {}".format(self.name, share))
        share_sema.release()


if __name__ == '__main__':
    share = 0
    tds = [MyThread("Threading%s" % i) for i in range(5)]
    for td in tds:
        td.start()
