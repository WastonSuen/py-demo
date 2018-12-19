# coding=utf-8
"""
@version: 2018/2/22 022
@author: Suen
@contact: sunzh95@hotmail.com
@file: multiprocessing_queue
@time: 21:45
@note:  Queue, FIFO, 支持多个进程入队列出队列
"""

import time
from multiprocessing import Process, Queue
from queue import Empty

from typing import Iterable


class ProducerProcess(Process):
    def __init__(self, queue, params):
        super(ProducerProcess, self).__init__()
        self.queue = queue
        self.params = params

    def run(self):
        if isinstance(self.params, Iterable):
            for param in self.params:
                print('put in: %s' % param)
                self.queue.put(param)
                time.sleep(1)
        else:
            print('put in: %s' % self.params)
            self.queue.put(self.params)
            time.sleep(1)


class ComsumerProcess(Process):
    def __init__(self, queue):
        super(ComsumerProcess, self).__init__()
        self.queue = queue

    def run(self):
        while 1:
            try:
                param = self.queue.get(timeout=2)
                print('get out: %s' % param)
                time.sleep(1)
            except Empty as e:
                print('queue is empty now')
                break


if __name__ == '__main__':
    queue = Queue()
    params = range(10)
    producer = ProducerProcess(queue=queue, params=params)
    comsumer = ComsumerProcess(queue=queue)
    producer.start()
    comsumer.start()
    producer.join()
    comsumer.join()
