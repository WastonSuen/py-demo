# coding=utf-8
"""
@version: 2017/12/15 015
@author: Suen
@contact: sunzh95@hotmail.com
@file: write_cvs
@time: 18:30
@note:  solve the chinese encoding problem
"""
#

import codecs
import csv

data = {}
filepath = './t.csv'
with codecs.open(filepath, 'ab+', 'utf_8_sig') as f:
    writer = csv.writer(f)
    writer.writerow(['col1', 'col2'])
    for k, v in data.items():
        if not any(v):
            continue
        writer.writerow(['val1', 'val2'])
