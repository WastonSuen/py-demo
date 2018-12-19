# coding=utf-8
"""
@version: 2017/11/23 023
@author: Suen
@contact: sunzh95@hotmail.com
@file: emailserv
@time: 11:49
@note:  ??
"""
#

import datetime
import smtplib
from email.mime.text import MIMEText

DEFAULT_EMAIL_HOST = ''
DEFAULT_EMAIL_PORT = ''
DEFAULT_EMAIL_HOST_USER = ''
DEFAULT_EMAIL_HOST_PASSWORD = ''


class MailServer(object):
    HOST = DEFAULT_EMAIL_HOST
    POST = DEFAULT_EMAIL_PORT
    USER = DEFAULT_EMAIL_HOST_USER
    PWD = DEFAULT_EMAIL_HOST_PASSWORD
    TO_ADDRS = ['sunzh95@hotmail.com', ]

    def __init__(self, host=None, port=None):
        self.host = host or self.HOST
        self.port = port or self.POST
        self.debuglevel = 1
        self.server = smtplib.SMTP_SSL(self.host, self.port)

    def login(self, user=None, pwd=None):
        self.user = user or self.USER
        self.pwd = pwd or self.PWD
        self.server.set_debuglevel(self.debuglevel)

    def send_mail(self, title, message, to_addrs=None):
        self.to_addrs = to_addrs or self.TO_ADDRS
        self.message = str(message) + '\n\n\n' + datetime.datetime.now().isoformat()
        self.msg = MIMEText(self.message, 'plain', 'utf-8')
        self.msg['From'] = self.user
        self.msg['To'] = ','.join(self.to_addrs)
        self.msg['Subject'] = str(title)

        self.server.login(self.user, self.pwd)
        self.server.sendmail(self.user, self.to_addrs, self.msg.as_string())
        self.server.quit()


mail_server = MailServer()

if __name__ == '__main__':
    msg = datetime.datetime.now().strftime('%Y-%m-%d\n') + '\n'.join(['s', 'w', 'm'])

    mail_server.send_mail('mail_test', msg, ['sunzh95@hotmail.com', ])
