# coding=utf-8
"""
@version: 2018/3/6
@author: Suen
@contact: sunzh95@hotmail.com
@file: linked_list
@time: 23:34
@note:  

1.数组(顺序表)：
数组是将元素在内存中连续存放，由于每个元素占用内存相同，可以通过下标迅速访问数组中任何元素。但是如果要
在数组中增加一个元素，需要移动大量元素，在内存中空出一个元素的空间，然后将要增加的元素放在其中。同样的
道理，如果想删除一个元素，同样需要移动大量元素去填掉被移动的元素。

如果应用需要快速访问数据，很少插入和删除元素，就应该用数组。

2.链表：
链表中的元素在内存中不是顺序存储的，而是通过存在元素中的指针联系到一起，每个结点包括两个部分：一个是存
储数据元素 的数据域，另一个是存储下一个结点地址的 指针。如果要访问链表中一个元素，需要从第一个元素始，
一直找到需要的元素位置。但是增加和删除一个元素对于链表数据结构就非常简单了，只要修改元素中的指针就可以
了。

如果应用需要经常插入和删除元素你就需要用链表

"""


class Node(object):
    def __init__(self, value, pnext=None):
        self.value = value
        self._next = pnext


class LinkedList(object):
    def __init__(self, node):
        if isinstance(node, Node):
            self.head = node
            self.length = 1
        else:
            self.head = None
            self.length = 0

    def append(self, node):
        item = node if isinstance(node, Node) else Node(node)
        if not self.head:
            self.head = item
        else:
            current_node = self.head
            while current_node._next:
                current_node = current_node._next
            current_node._next = item
        self.length += 1
        return True

    def pop(self):
        current_node = self.head
        for _ in range(self.length - 2):
            current_node = current_node._next

        value = current_node._next.value
        del current_node._next
        current_node._next = None
        self.length -= 1
        return value

    def get_index(self, value):
        current_node = self.head
        i = 0
        while current_node:
            if value == current_node.value:
                return i
            current_node = current_node._next
            i += 1
        return None

    def get_item(self, k):
        if k < 0 or k >= self.length:
            raise ValueError('index out of range')
        current_node = self.head
        for _ in range(k):
            current_node = current_node._next
        return current_node.value

    def insert(self, k, node):
        item = node if isinstance(node, Node) else Node(node)
        if not self.head or k == self.length:
            return self.append(item)
        if k > self.length:
            raise ValueError('index out of range')

        current_node = self.head
        if k == 0:
            item._next = current_node
            self.head = item
        elif 0 < k and k <= self.length - 1:
            for _ in range(k - 1):
                current_node = current_node._next
            item._next = current_node._next
            current_node._next = item
        self.length += 1
        return True

    def remove(self, k):
        if not self.head:
            print('linked list is already empty')
            return True
        if k > self.length - 1:
            raise ValueError('index out of range')
        if k == self.length - 1:
            return self.pop()

        current_node = self.head
        if k == 0:
            self.head = current_node._next
        elif 0 < k and k < self.length - 1:
            for _ in range(k - 1):
                current_node = current_node._next
            current_node._next = current_node._next._next
        value = current_node.value
        del current_node
        self.length -= 1
        return value

    def update(self, k, node):
        """
        两种update方案, 一种是只更新node的value值, 此种方法较为简单, 此处不作讨论。另一种是更新node, 方法如下 
        :param k: 0<=k<=self.length-1
        :param node: 
        :return: 
        """
        item = node if isinstance(node, Node) else Node(node)
        if not self.head:
            self.append(item)
        if k == self.length - 1:
            self.pop()
            self.append(item)
        if k == 0:
            item._next = self.head._next
            del self.head._next
            self.head = item
        elif 0 < k and k < self.length - 1:
            curreent_node = self.head
            for _ in range(k - 1):
                curreent_node = curreent_node._next
            item._next = curreent_node._next._next
            del curreent_node._next
            curreent_node._next = item

    def __reversed__(self):
        """
        翻转单向链表, 一种方法是可以遍历改变指针指向, 代码如下; 
        另一种方法是新建栈(A), 遍历原单向链表, 全部入栈A, 再出栈A建立新的链表,
          就得到逆序的原链表。 同理, 可以使用两个栈来实现队列的功能
        :return: 
        """
        if self.length in [0, 1]:
            return self
        current_node = self.head
        next_node = current_node._next
        current_node._next = None  # 单独消除首节点的环
        while next_node and next_node._next:
            temp_node = current_node
            current_node = next_node
            next_node = next_node._next
            current_node._next = temp_node
        next_node._next = current_node  # 单独处理尾节点
        del self.head, current_node
        self.head = next_node  # 尾节点变首节点

    def __repr__(self):
        current_node = self.head
        values = []
        while current_node:
            values.append(current_node.value)
            current_node = current_node._next
        return str(values)


if __name__ == '__main__':
    linked_list = LinkedList(Node(0))
    linked_list.append(Node(1))
    linked_list.append(Node(2))
    linked_list.append(3)
    linked_list.pop()
    linked_list.update(1, 4)
    linked_list.remove(0)
    linked_list.insert(0, 5)
    print(linked_list)
    reversed(linked_list)
    print(linked_list)
    print(linked_list.get_item(1))
    print(linked_list.get_index(4))
    print(linked_list.get_index(3))
