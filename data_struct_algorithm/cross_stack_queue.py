# coding=utf-8
"""
@version: 2018/3/7 007
@author: Suen
@contact: sunzh95@hotmail.com
@file: cross_stack_queue
@time: 17:44
@note:  ??
"""

from daily.data_struct_algorithm.stack_and_queue import Stack, Queue


class QueueBy2Stack(object):
    stack_one = Stack()
    stack_two = Stack()
    convert = False

    def push(self, value):
        self.stack_one.push(value)
        self.convert = False

    def _convert(self):
        """
        每次pop之前, 如果有新的push, 都要调用_convert 
        把栈stack_one pop并push进 stack_two
        :return: 
        """
        if self.stack_two.top is not None:
            i = 0
            while self.stack_one.top is not None:
                self.stack_two.insert(self.stack_one.pop(), k=i)
                i += 1
        else:
            while self.stack_one.top is not None:
                self.stack_two.push(self.stack_one.pop())
        self.convert = True

    def pop(self):
        if not self.convert:
            self._convert()
        return self.stack_two.pop()


class StackBy2Queue(object):
    """
    保证取出元素的时候都选择length为1的queue, 优先选择入队队列(queue_one)
    """
    queue_one = Queue()
    queue_two = Queue()
    flag = False

    def push(self, value):
        """
        每次push 保证queue_one只存在最多只存在1个元素, pop时优先选择queue_one
        :param value: 
        :return: 
        """
        self.queue_one.push(value)
        self.flag = True
        if self.queue_one.length > 1:
            self.queue_two.push(self.queue_one.popleft())

    def pop(self):
        value = None
        if self.flag and self.queue_one.length == 1:
            self.flag = False
            return self.queue_one.popleft()
        elif not self.queue_one.length and self.queue_two.length:
            while self.queue_two.length > 1:
                self.queue_one.push(self.queue_two.popleft())

            value = self.queue_two.popleft()
            self.queue_two.head = self.queue_one.head
            self.queue_two.length = self.queue_one.length
            self.queue_one.clear()
            self.flag = False

            # 如果选择queue_two pop, 且只剩下一个元素，则push进queue_one, 保证下一次push正确
            if self.queue_two.length == 1:
                self.queue_one.push(self.queue_two.popleft())
                self.flag = True
        return value


if __name__ == '__main__':
    qbs = QueueBy2Stack()
    qbs.push(1)
    qbs.push(2)
    print(qbs.pop())
    qbs.push(3)
    qbs.push(4)
    print(qbs.pop())
    print(qbs.pop())
    qbs.push(5)
    print(qbs.pop())
    print(qbs.pop())

    sbq = StackBy2Queue()
    sbq.push(1)
    sbq.push(2)
    print(sbq.pop())
    sbq.push(3)
    sbq.push(4)
    print(sbq.pop())
    sbq.push(5)
    print(sbq.pop())
    print(sbq.pop())
    print(sbq.pop())
    print(sbq.pop())
