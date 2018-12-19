# coding=utf-8
"""
@version: 2018/3/8 008
@author: Suen
@contact: sunzh95@hotmail.com
@file: binary_tree
@time: 17:24
@note:  ??
"""
from daily.data_struct_algorithm.stack_and_queue import Queue, Stack


class BinaryNode(object):
    def __init__(self, key, lchild=None, rchild=None):
        self.key = key
        self.lchild = lchild
        self.rchild = rchild

    def __repr__(self):
        return '<Binary Node, key:{}>\n lchild:{}\n rchild:{}'.format(self.key, self.lchild, self.rchild)


class BinaryTree(object):
    def __init__(self, item):
        self.root = BinaryNode(item)
        self.size = 1

    def normal_add(self, item):
        node = BinaryNode(item)

        pre_list = [self.root]
        self.size += 1
        while True:
            root = pre_list.pop(0)  # 列表取出index为0的元素, 时间复杂度为O(n)
            if root.lchild is None:
                root.lchild = node
                break
            elif root.rchild is None:
                root.rchild = node
                break
            else:
                pre_list.append(root.lchild)
                pre_list.append(root.rchild)

    def normal_traverse(self):
        """
        层次遍历
        :return: 
        """
        traverse_list = [self.root]
        while traverse_list:
            root = traverse_list.pop(0)
            print(root.key)
            if root.lchild is not None:
                traverse_list.append(root.lchild)
            if root.rchild is not None:
                traverse_list.append(root.rchild)

    def add(self, item):
        """
        添加元素, 队列实现
        :param item:
        :return:
        """
        node = BinaryNode(item)
        queue = Queue(self.root)
        self.size += 1
        while True:
            root = queue.popleft()
            if root.lchild is None:
                root.lchild = node
                break
            elif root.rchild is None:
                root.rchild = node
                break
            else:
                queue.push(root.lchild)
                queue.push(root.rchild)

    def traverse(self):
        """
        层次遍历, 队列实现
        :return:
        """
        traverse_queue = Queue(self.root)
        traverse_result = []
        while traverse_queue.length > 0:
            root = traverse_queue.popleft()
            traverse_result.append(root.key)
            if root.lchild is not None:
                traverse_queue.push(root.lchild)
            if root.rchild is not None:
                traverse_queue.push(root.rchild)
        return traverse_result

    def pre_traverse(self):
        """
        先序遍历, list实现, 或Stack实现也可
        :return:
        """
        pre_traverse_list = [self.root]
        traverse_result = []
        while pre_traverse_list:
            root = pre_traverse_list.pop()
            traverse_result.append(root.key)
            if root.rchild is not None:
                pre_traverse_list.append(root.rchild)
            if root.lchild is not None:
                pre_traverse_list.append(root.lchild)
        return traverse_result

    def in_traverse(self, root=None):
        """
        中序遍历,
        :return: 
        """
        if not root: root = self.root
        left_list = []
        right_list = []
        if root.lchild: left_list += self.in_traverse(root.lchild)
        if root.rchild: right_list += self.in_traverse(root.rchild)
        return left_list + [root.key] + right_list

    def after_traverse(self, root=None):
        """
        后序遍历
        :param root: 
        :return: 
        """
        if not root: root = self.root
        left_list = []
        right_list = []
        if root.lchild: left_list += self.after_traverse(root.lchild)
        if root.rchild: right_list += self.after_traverse(root.rchild)
        return left_list + right_list + [root.key]


if __name__ == '__main__':
    bt = BinaryTree(0)
    bt.add(1)
    bt.add(2)
    bt.add(3)
    bt.add(4)
    bt.add(5)
    bt.add(6)
    bt.add(7)
    bt.add(8)
    bt.add(9)

    print(bt.traverse())
    print(bt.pre_traverse())
    print(bt.in_traverse())
    print(bt.after_traverse())
