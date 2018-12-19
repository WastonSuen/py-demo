#!/usr/bin/python
# coding=utf-8
"""
@version: 2017/11/18 018
@author: Suen
@contact: sunzh95@hotmail.com
@file: download_video
@time: 9:40
@note:  ??
"""
#

import os
import json
import urllib
import socket
import threading
import urllib.request

socket.setdefaulttimeout(60)  # urllib timeout


class MyThread(threading.Thread):
    def __init__(self, i):
        super(MyThread, self).__init__()
        self.i = i
        self.url = base_url % i
        self.filename = self.url.split('/')[-1]
        num_set.add(self.i)
        self.file = os.path.join(dir_path, self.filename).encode('gbk')

    def run(self):
        print('start %s' % self.filename)
        try:
            urllib.request.urlretrieve(self.url, self.file)
        except:
            'err happened when processing {}'.format(self.i)
        else:
            print('done %s' % self.filename)
            num_set.remove(self.i)


def process(num_set):
    tds = []
    for i in num_set: tds.append(MyThread(i))

    for td in tds: td.start()

    for td in tds: td.join()


def batch_download(url_list, path):
    global base_url, num_set, dir_path
    base_url = '%s'
    dir_path = path

    if not os.path.exists(dir_path.encode('gbk')):
        os.mkdir(dir_path.encode('gbk'))
    num_set = set(url_list)
    while num_set:
        process(num_set)
        if num_set:
            print('failed file(s) Number set:%s\nauto retrying...\n' % json.dumps(list(num_set)))

    print('all done')


if __name__ == '__main__':
    dir_name = 'jiqixuexi'
    dir_path = os.path.join(os.path.abspath('.'), dir_name)
    base_url = 'http://newoss.maiziedu.com/qiniu/jqxx-%02d.mp4'

    num_set = set(range(1, 28))
    process(num_set)

    while num_set:
        print('failed file(s) Number set:%s\nauto retrying...\n' % json.dumps(list(num_set)))
        process(num_set)

    print('all done')
