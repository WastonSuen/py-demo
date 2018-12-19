# coding=utf-8
"""
@version: 2017/12/13 013
@author: Suen
@contact: sunzh95@hotmail.com
@file: threading_conditionlock
@time: 12:11
@note:  封装了Lock, Rlock, 有了wait, notify等特性, notify 并不会释放占用的锁
"""
#

import threading
import time

share_cond = threading.Condition()


class Producer(threading.Thread):
    def __init__(self, i):
        super(Producer, self).__init__()
        self.name = 'Producer%s' % i

    def run(self):
        global share
        if share_cond.acquire():
            while True:
                if not share:
                    print('{}, share: {}'.format(self.name, share))
                    share += 1
                else:
                    print('{}, share: {}, Not Operation'.format(self.name, share))
                share_cond.notify()
                share_cond.wait()
                time.sleep(1)


class Consumer(threading.Thread):
    def __init__(self, i):
        super(Consumer, self).__init__()
        self.name = 'Consumer%s' % i

    def run(self):
        global share
        if share_cond.acquire():
            while True:
                if share:
                    print('{}, share: {}'.format(self.name, share))
                    share -= 1
                else:
                    print('{}, share: {}, Not Operation'.format(self.name, share))
                share_cond.notify()
                share_cond.wait()
                time.sleep(1)


if __name__ == '__main__':
    share = 0
    producers = [Producer(i) for i in range(1, 5)]
    consumers = [Consumer(i) for i in range(1, 5)]
    [producer.start() for producer in producers]
    [consumer.start() for consumer in consumers]
