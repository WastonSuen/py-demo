# coding=utf-8
"""
@version: 2018/2/22 022
@author: Suen
@contact: sunzh95@hotmail.com
@file: multiprocessing_pipe
@time: 22:16
@note:  Pipe, FIFO, 只允许两点传输
"""

import time
from multiprocessing import Process, Pipe
from typing import Iterable


class ProducerProcess(Process):
    def __init__(self, pipe, msgs):
        super(ProducerProcess, self).__init__()
        self.pipe = pipe
        self.msgs = msgs

    def run(self):
        if isinstance(self.msgs, Iterable):
            for msg in self.msgs:
                print('send msg: %s' % msg)
                self.pipe.send(msg)
                time.sleep(1)
        else:
            print('send msg: %s' % self.msgs)
            self.pipe.send(self.msgs)
            time.sleep(1)


class ComsumerProcess(Process):
    def __init__(self, pipe):
        super(ComsumerProcess, self).__init__()
        self.pipe = pipe

    def run(self):
        while 1:
            try:
                assert self.pipe.poll() == True
                msg = self.pipe.recv()
                print('recv msg: %s' % msg)
                time.sleep(1)
            except AssertionError:
                print('all done')
                break


if __name__ == '__main__':
    sender, receiver = Pipe()
    producer = ProducerProcess(sender, range(10))
    comsumer = ComsumerProcess(receiver)
    producer.start()
    comsumer.start()
    producer.join()
    comsumer.join()
