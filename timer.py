# -*- coding: utf-8 -*-

# ********************************************************** #
# *********************single timer************************* #
# ********************************************************** #

import monotonic


class Timer(object):
    def __init__(self, excute_obj=''):
        self.excete_obj = excute_obj

    def __enter__(self):
        self.__start = monotonic.monotonic()

    def __exit__(self, type, value, traceback):
        self.__finish = monotonic.monotonic()
        print 'timer <%s> time expends: %s s' % (
            self.excete_obj, self.duration_in_seconds())

    def duration_in_seconds(self):
        return self.__finish - self.__start


# ********************************************************** #
# *********************time collector*********************** #
# ********************************************************** #

TIME = 0
import functools
import monotonic


def time_collector():
    def wrapper(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            _start = monotonic.monotonic()
            res = func(*args, **kwargs)
            _end = monotonic.monotonic()
            expire = _end - _start
            global TIME
            TIME += expire
            print "time_collector <%s> expends: %s s" % (func.__name__, TIME)
            return res

        return _wrapper

    return wrapper
