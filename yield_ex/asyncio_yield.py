# coding=utf-8
"""
@version: 2018/1/31 031
@author: Suen
@contact: sunzh95@hotmail.com
@file: asyncio_yield
@time: 14:45
@note:  async/await 与 asyncio.coroutine/yield from等效, 前者用于协程, 后者用于生成器
"""
import asyncio
import random


# @asyncio.coroutine
# def smart_fib(n):
#     index = 0
#     a = 0
#     b = 1
#     while index < n:
#         sleep_secs = random.uniform(0, 0.2)
#         yield from asyncio.sleep(sleep_secs)
#         print('Smart one think {} secs to get {}'.format(sleep_secs, b))
#         a, b = b, a + b
#         index += 1

async def smart_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0, 0.2)
        await asyncio.sleep(sleep_secs)
        print('Smart one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1


# @asyncio.coroutine
# def stupid_fib(n):
#     index = 0
#     a = 0
#     b = 1
#     while index < n:
#         sleep_secs = random.uniform(0.2, 0.4)
#         yield from asyncio.sleep(sleep_secs)
#         print('Stupid one think {} secs to get {}'.format(sleep_secs, b))
#         a, b = b, a + b
#         index += 1

async def stupid_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0.2, 0.4)
        await asyncio.sleep(sleep_secs)
        print('Stupid one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        asyncio.ensure_future(smart_fib(10)),
        asyncio.ensure_future(stupid_fib(10)),
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    print('All fib finished.')
    loop.close()
