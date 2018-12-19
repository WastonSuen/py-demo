# coding=utf-8
"""
@version: 2017/12/12 012
@author: Suen
@contact: sunzh95@hotmail.com
@file: socket_udp_srv
@time: 14:42
@note:  ??
"""
#

import socket

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 12345
    srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    srv.bind((HOST, PORT))
    while True:
        data, addr = srv.recvfrom(1024)
        print("Received Data: {}".format(data.decode('utf-8')))
        srv.sendto(data, addr)
        if data == b'Bye':
            break

    srv.close()
