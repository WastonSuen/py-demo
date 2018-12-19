# coding=utf-8
"""
@version: 2017/12/15 015
@author: Suen
@contact: sunzh95@hotmail.com
@file: err_log_mailer
@time: 18:27
@note:  ??
"""
#

import os
import re
import datetime
import smtplib

path_format = {
    "server1": "server_location1",
    "server2": "server_location2",
    "server3": "server_location3",
}

partten = "^\[(?P<dt>\d{4}-\d{2}-\d{2},\d{2}:\d{2}:\d{2}:\d{3})\] (?P<fl>[\w\d_\.]+:\d+) (?P<n>[\w ]+),(?P<info>.*)$"
pds = path_format.keys()


def stat_data(date):
    result = dict((pd, {}) for pd in pds)

    for pd in pds:
        path = path_format[pd] % dict(pd=pd, date=date)
        if not os.path.exists(path):
            continue
        with open(path, 'rb') as f:
            for line in f:
                try:
                    data = re.match(partten, line).groupdict()
                    file_line = data['fl']
                    result[pd].setdefault(file_line, [0, ''])
                    result[pd][file_line][0] += 1
                    result[pd][file_line][1] = data['n']
                except:
                    pass
    return result


def make_text(data):
    buffer = []
    for k, v in data.items():
        buffer.append("[%s_err.log]" % k)

        for k, v in sorted(v.items(), key=lambda x: x[1][0], reverse=True):
            buffer.append("<%s> %s" % (k, v))
        buffer.append("\n")
    return "\n".join(buffer)


def main(date):
    data = stat_data(date)
    content = make_text(data)

    smtp_host = "smtp.exmail.qq.com"
    smtp_port = 465

    from_addr = ""
    password = ''
    to_addrs = ['sunzh95@hotmail.com', ]

    smtp_obj = smtplib.SMTP_SSL()
    smtp_obj.connect(smtp_host, smtp_port)

    smtp_obj.login(from_addr, password)

    from email.mime.text import MIMEText
    from email.header import Header

    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header("192.168.2.154", 'utf-8')

    message['Subject'] = Header("server_err_log%s" % date, 'utf-8')

    smtp_obj.sendmail(from_addr, to_addrs, message.as_string())
    smtp_obj.close()


if __name__ == '__main__':
    date = datetime.date.today().isoformat()
    main(date)
