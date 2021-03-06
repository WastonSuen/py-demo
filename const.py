# coding=utf-8
"""
@version: 2017/12/8 008
@author: Suen
@contact: sunzh95@hotmail.com
@file: PyConst
@time: 10:15
@note:  const in python
"""
#

import sys


class Const(object):
    class ConstError(TypeError):
        def __init__(self, name):
            self.msg = "Can't rebind const instance attribute (%s)" % name

        def __str__(self):
            return 'error msg: {}'.format(self.msg)

        def __repr__(self):
            return self.__str__()

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError(name)

        self.__dict__[name] = value

    def __delattr__(self, name):
        if self.__dict__.has_key(name):
            raise self.ConstError(name)

        raise self.ConstError(name)


sys.modules[__name__] = Const()
