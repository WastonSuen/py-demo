# coding=utf-8
"""
@version: 2018/3/6 006
@author: Suen
@contact: sunzh95@hotmail.com
@file: search
@time: 10:51
@note:  ??
"""
from daily.clockdeco import clock


@clock
def bisect_search(search_list, value, search_gap=1 / 2, low=0, high=0):
    """
    二分查找， O(lgn)
    :param search_list: 
    :param value: 
    :param search_gap: 
    :param low: 
    :param high: 
    :return: 
    """
    if not search_list:
        return
    length = len(search_list[low:high])
    while low < high:
        mid = int((low + high) * search_gap)
        if search_list[mid] < value:
            return bisect_search(search_list, value, low=mid + 1, high=low + length)
        elif search_list[mid] > value:
            return bisect_search(search_list, value, low=low, high=mid)
        else:
            return mid, search_list[mid]
    return low, search_list[low]


@clock
def insertion_search(search_list, value, low=0, high=0):
    """
    插值查找, O(lgn), 适用于均匀分布的排序列表, 此时优于二分查找
    :param search_list: 
    :param value: 
    :param low: 
    :param high: 
    :return: 
    """
    search_gap = (value - search_list[low]) / (search_list[high - 1] - search_list[low])
    return bisect_search(search_list, value, search_gap, low=0, high=len(search_list))


@clock
def fibonacci_search(search_list, value):
    """
    Fibonacci查找, O(log(n)), 平均性能优于二分查找, 如果查找值在列表最左侧, 则性能最低
    :param search_list: 
    :param value: 
    :return: 
    """
    length = len(search_list)

    def fib(nums=10):
        a, b = 0, 1
        i = 0
        while a < nums:
            yield b
            i += 1
            a, b = b, a + b

    fibonacci_list = [f for f in fib(nums=length)]
    while fibonacci_list[-1] > length:
        search_list.append(search_list[-1])
        length += 1

    low = 0
    high = length

    # 此处从右往左查找
    k = len(fibonacci_list)
    while low <= high:
        mid = low if k < 2 else low + fibonacci_list[k - 1] - 1
        if value < search_list[mid]:
            high = mid - 1
            k -= 1
        elif value > search_list[mid]:
            low = mid + 1
            k -= 2
        else:
            return mid
    return False

"""
二分查找的mid运算是加法与除法，插值查找则是复杂的四则运算，而斐波那契查找只是最简单的加减运算。
在海量数据的查找中，这种细微的差别可能会影响最终的查找效率。
因此，三种有序表的查找方法本质上是分割点的选择不同，各有优劣，应根据实际情况进行选择。
"""



if __name__ == '__main__':
    l = [v for v in range(50)]
    print(bisect_search(l, 10, high=len(l)))
    print(insertion_search(l, 28, low=0, high=len(l)))
    print(fibonacci_search(l, 1))
