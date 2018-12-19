# coding=utf-8
"""
@version: 2017/12/13 013
@author: Suen
@contact: sunzh95@hotmail.com
@file: threading_join
@time: 11:38
@note:  ??
"""
#

import time
import threading
from daily.clockdeco import clock


class MyThread(threading.Thread):
    def run(self):
        for i in range(30):
            print("Threading {}".format(i))
            time.sleep(0.1)


@clock
def main():
    td = MyThread()
    # td.setDaemon(True)  # 设置为后台线程，主线程结束时自杀
    td.start()
    # td.join()#等待子线程执行完毕，再执行后续程序

    for i in range(10):
        print("Main {}".format(i))
        time.sleep(0.1)


if __name__ == '__main__':
    main()
