# coding=utf-8
"""
@version: 2018/2/16 016
@author: Suen
@contact: sunzh95@hotmail.com
@file: regular_pattern
@time: 20:55
@note:  ??
"""

import re

email_pattern = r'^[A-Za-z][A-Za-z0-9_]+@[A-Za-z0-9_]+\.[(cn)|(com)]+$'
ip_pattern = r'(?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d)'
