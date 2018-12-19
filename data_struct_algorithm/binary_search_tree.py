# coding=utf-8
"""
@version: 2018/3/12 012
@author: Suen
@contact: sunzh95@hotmail.com
@file: binary_search_tree
@time: 16:11
@note:  ??
"""

from daily.data_struct_algorithm.binary_tree import BinaryTree, BinaryNode


class BinarySearchTree(BinaryTree):
    def insert(self, key):
        node = BinaryNode(key)
        root = self.root
        while root is not None:
            if root.key == key:
                raise ValueError('key conflict')
            elif root.key > key:
                if root.lchild is None:
                    root.lchild = node
                    return root
                else:
                    root = root.lchild
            elif root.key < key:
                if root.rchild is None:
                    root.rchild = node
                    return root
                else:
                    root = root.rchild
        return None

    def search(self, key):
        """
        有递归实现与迭代实现两种, 此处为迭代实现
        :param key: 
        :return: 
        """
        root = self.root
        while root is not None:
            if root.key == key:
                return root
            elif root.key > key:
                root = root.lchild
            elif root.key < key:
                root = root.rchild
        return None

    def delete(self, key, parent=None):
        root = self.root
        if root.key == key:
            self.root = root.lchild or root.rchild
            del root
            return True

        while root is not None:
            # TODO fix this condition
            if root.key == key:
                if root.lchild is not None and root.rchild is None:
                    parent.lchild = root.lchild
                elif root.rchild is not None and root.lchild is None:
                    parent.rchild = root.rchild
                elif root.lchild is None and root.rchild is None:
                    pass
                del root
                return True

            elif root.key > key:
                if root.lchild is None:
                    return False
                parent = root
                root = root.lchild
            elif root.key < key:
                if root.rchild is None:
                    return False
                parent = root
                root = root.rchild


if __name__ == '__main__':
    bst = BinarySearchTree(5)
    bst.insert(4)
    bst.insert(6)
    bst.insert(2)
    bst.insert(3)
    bst.insert(1)
    print(bst.search(5))
    bst.delete(1)
    print(bst.search(5))
