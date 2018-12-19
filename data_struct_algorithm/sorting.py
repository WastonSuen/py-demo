# coding=utf-8
"""
@version: 2018/3/5 005
@author: Suen
@contact: sunzh95@hotmail.com
@file: sorting
@time: 15:52
@note:  python 实现排序算法
"""
from daily.clockdeco import clock


@clock
def bubble(sort_list):
    """
    冒泡排序, T(n)=O(n^2), 每次遍历都选出最小的放到i处
    :param sort_list: 
    :return: 
    """
    length = len(sort_list)
    for i in range(length - 1):
        exchange = False  # 如果已经排好序, 就提前返回
        for j in range(i + 1, length):
            if sort_list[i] > sort_list[j]:
                sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
                exchange = True
        if exchange == False:
            return sort_list
    return sort_list


@clock
def select_sorting(sort_list):
    """
    选择排序, T(n)=O(n^2), 和冒泡排序类似, 显示的选择出最小的元素, 减少了列表的值交换过程
    :param sort_list: 
    :return: 
    """
    length = len(sort_list)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if sort_list[min_index] > sort_list[j]:
                min_index = j
        if min_index == i:
            return sort_list
        sort_list[i], sort_list[min_index] = sort_list[min_index], sort_list[i]
    return sort_list


@clock
def insertion_sorting(sort_list):
    """
    插入排序, T(n)=O(n^2), 分为有序部分, 无序部分来排序
    :param sort_list: 
    :return: 
    """
    length = len(sort_list)
    for i in range(1, length):
        exchange_index = i  # 未排序部分的元素
        for j in range(i - 1, -1, -1):  # 逆序遍历已排序部分
            if sort_list[exchange_index] < sort_list[j]:
                # 找到第一个比待排序元素小的元素,交换
                sort_list[exchange_index], sort_list[j] = sort_list[j], sort_list[exchange_index]
    return sort_list


@clock
def quick_sorting(sort_list):
    """
    快速排序, T(n)=[O(nlgn), O(n^2)], 从两端向中间同时遍历, 递归
    :param sort_list: 
    :return: 
    """

    def partition(sort_list, left=0, right=len(sort_list) - 1):
        temp = sort_list[left]
        while left < right:
            while left < right and temp < sort_list[right]:
                # 右边值较小时, temp不动, 左移right
                right -= 1
            sort_list[left] = sort_list[right]  # 否则移动到左边
            while left < right and temp > sort_list[left]:
                # 左边值较小时,temp不动, 右移left
                left += 1
            sort_list[right] = sort_list[left]
        sort_list[left] = temp
        return left

    def sub_quick_sorting(sort_list, left=0, right=len(sort_list) - 1):
        if left < right:
            mid = partition(sort_list, left, right)
            sub_quick_sorting(sort_list, left, mid - 1)
            sub_quick_sorting(sort_list, mid + 1, right)

    sub_quick_sorting(sort_list)
    return sort_list


@clock
def heap_sorting(sort_list):
    """
    堆排序, 完全二叉树排序, T(n)=O(nlgn)
    :param sort_list: 
    :return: 
    """

    def adjust_map_heap(sort_list, i, size):
        lchild = 2 * i + 1
        rchild = 2 * i + 2
        max_index = i
        if i < size / 2:
            if lchild < size and sort_list[lchild] > sort_list[max_index]:
                max_index = lchild
            if rchild < size and sort_list[rchild] > sort_list[max_index]:
                max_index = rchild
            if max_index != i:
                sort_list[max_index], sort_list[i] = sort_list[i], sort_list[max_index]
                adjust_map_heap(sort_list, max_index, size)

    def build_map_heap(sort_list, size):
        for i in range((size // 2) - 1, -1, -1):
            adjust_map_heap(sort_list, i, size)

    size = len(sort_list)
    build_map_heap(sort_list, size)
    for i in range(size - 1, -1, -1):
        sort_list[i], sort_list[0] = sort_list[0], sort_list[i]
        adjust_map_heap(sort_list, 0, i)
    return sort_list


@clock
def merge_sorting(sort_list):
    """
    归并排序, T(n)=O(nlgn), 先拆分, 再排序, 再合并
    :param sort_list:
    :return:
    """

    def merge(sort_list1, sort_list2):
        i = j = 0
        len1 = len(sort_list1)
        len2 = len(sort_list2)
        result = []
        while i <= len1 - 1 and j <= len2 - 1:
            if sort_list1[i] < sort_list2[j]:
                result.append(sort_list1[i])
                i += 1
            else:
                result.append(sort_list2[j])
                j += 1
        if i != len1:
            result += sort_list1[i:]
        if j != len2:
            result += sort_list2[j:]
        return result

    def split_merge(sort_list):
        length = len(sort_list)
        if length == 1:
            return merge(sort_list, [])
        else:
            return merge(split_merge(sort_list[0:length // 2] or []), split_merge(sort_list[length // 2:] or []))

    result = split_merge(sort_list)
    return result


@clock
def radix_sorting(sort_list, k=3):
    """
    基数排序, T(n)=O(nlgn), 分桶排序
    :param sort_list:
    :param k:
    :return:
    """
    for kk in range(k):
        bucket = [[] for i in range(10)]
        for param in sort_list:
            bucket[int((param / (10 ** kk)) % 10)].append(param)  # 依次按个位数，十位数...放入相应的桶
        sort_list = [v for value in bucket for v in value]
    return sort_list


if __name__ == '__main__':
    l = [i for i in range(500, 0, -1)]
    # bubble(l)
    # select_sorting(l)
    # insertion_sorting(l)
    # quick_sorting(l)
    # heap_sorting(l)
    # merge_sorting(l)
    radix_sorting(l, k=3)
