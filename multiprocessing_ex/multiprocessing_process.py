# coding=utf-8
"""
@version: 2018/2/22 022
@author: Suen
@contact: sunzh95@hotmail.com
@file: multiprocessing_process
@time: 10:17
@note:  ??
"""

import time
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    def run(self):
        print('task <%s> is running' % self.name)
        time.sleep(2)
        print('task <%s> done' % self.name)


if __name__ == '__main__':
    print('main is running')
    p1 = MyProcess(name='p1')
    p2 = MyProcess(name='p2')
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('main is done')
