# coding=utf-8
"""
@version: 2017/12/25 025
@author: Suen
@contact: sunzh95@hotmail.com
@file: logger
@time: 16:05
@note:  ??
"""
import logging


def log():
    logger = logging.getLogger('main')
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(levelname)s - %(asctime)s - Process:%(process)d - thread:%(thread)d - %(filename)s - line:%(lineno)d - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


logger = log()
