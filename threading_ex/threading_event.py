# coding=utf-8
"""
@version: 2017/12/13 013
@author: Suen
@contact: sunzh95@hotmail.com
@file: threading_event
@time: 13:36
@note:  可挂起当前线程直到调用
"""
#

import threading
import time

share_event = threading.Event()


class WaitThread(threading.Thread):
    def run(self):
        self.name = 'wait_threading'
        print(self.name, 'waiting...')
        share_event.wait()
        print(self.name, 'starting...')
        for i in range(3):
            print('processing...')
            time.sleep(1)
        print(self.name, 'done\n')


class CommanderThread(threading.Thread):
    def run(self):
        time.sleep(3)
        self.name = 'commander_threading'
        print(self.name, 'send the starting order')
        share_event.set()


if __name__ == '__main__':
    wtd = WaitThread()
    ctd = CommanderThread()
    wtd.start()
    ctd.start()
