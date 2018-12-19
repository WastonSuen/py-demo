# coding=utf-8
"""
@version: 2018/2/1 001
@author: Suen
@contact: sunzh95@hotmail.com
@file: queue_ex.
@time: 16:56
@note:  ??
"""
import queue
import random
import operator


class Comparable(object):
    def __init__(self, priority):
        try:
            float(priority)
        except:
            raise ValueError('pripority must be int or float')
        self.priority = priority

    def __gt__(self, other):
        return operator.ge(self.priority, other.priority)

    def __lt__(self, other):
        return operator.lt(self.priority, other.priority)

    def __eq__(self, other):
        return operator.eq(self.priority, other.priority)


if __name__ == '__main__':
    q = queue.PriorityQueue()

    for i in range(10):
        q.put(Comparable(random.randint(1, 10)))

    while not q.empty():
        task = q.get()
        print(task.priority)
        q.task_done()
