# coding=utf-8
"""
@version: 2017/12/12 012
@author: Suen
@contact: sunzh95@hotmail.com
@file: socket_tcp_srv
@time: 14:35
@note:  ??
"""
#

import socket


def srv_service():
    HOST = '127.0.0.1'
    PORT = 12345
    srv = socket.socket()
    srv.bind((HOST, PORT))
    srv.listen(5)
    clnt, addr = srv.accept()
    print("Connectioned To Client: {}".format(addr))

    while True:
        data = clnt.recv(1024)
        print("Received From Client: {}".format(data.decode('utf-8')))
        clnt.send(data)
        if data == b'Bye':
            break

    clnt.close()
    srv.close()


if __name__ == '__main__':
    srv_service()
