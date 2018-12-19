# coding=utf-8
"""
@version: 2018/2/24 024
@author: Suen
@contact: sunzh95@hotmail.com
@file: subprocess
@time: 11:56
@note:  ??
"""

import subprocess

subprocess.Popen('a_time-need_command', shell=True, close_fds=True, stdout=open('/home/www/command.log', 'w+'))
# 开启新的子进程, 后台执行, close_fds表示子进程不继承父进程的输出输入, 不需等待
print('done')
