# coding=utf-8
"""
@version: 2018/2/11 011
@author: Suen
@contact: sunzh95@hotmail.com
@file: formatter
@time: 0:04
@note:  ??
"""
import re
import bson
import json
import base64
import hashlib
import datetime
from pymongo.cursor import Cursor

from daily.logger import logger


def encryptPwd(rawPwd):
    """
    密码加密闭包
    :param rawPwd: 
    :return: 
    """

    def md5Encrypt(raw, salt):
        m = hashlib.md5()
        m.update(raw)
        m.update(raw)
        m.update(salt)
        return m.hexdigest()

    return md5Encrypt(rawPwd, 'pwd_salt')


# 响应格式
handlers = {
    datetime.datetime: lambda o: str(o),
    bson.ObjectId: lambda o: str(o),
    Cursor: lambda o: list(o)
}


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        handler = handlers.get(type(o), json.JSONEncoder.default)
        return handler(o)


def decode_base64_file(b64string):
    imgType, others = b64string.split(';', 1)
    m = re.match(r'data:(?P<type>\w+)/(?P<ext>\w+)', imgType)
    dt = m.group('type')
    if dt.lower() != 'image':
        logger.error('Not Support Type:' + dt)
        return None, None
    ext = m.group('ext')
    encoding, data = others.split(',', 1)
    if encoding.lower() != 'base64':
        logger.error('Not Support Encoding:' + encoding)
        return None, None
    return base64.b64decode(data), ext
