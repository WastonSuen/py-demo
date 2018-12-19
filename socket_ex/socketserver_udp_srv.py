# coding=utf-8
"""
@version: 2017/12/14 014
@author: Suen
@contact: sunzh95@hotmail.com
@file: socketserver_udp_srv
@time: 11:31
@note:  ??
"""
#

__metaclass__ = type

import threading
import socketserver


class MyHandle(socketserver.DatagramRequestHandler):
    def handle(self):
        data, socket = self.request
        print("Received: {}".format(data.decode('utf-8')))
        socket.sendto(data, self.client_address)

        if data in (b'Bye', b'Bye\n'):
            print('server terminated')
            td = threading.Thread(target=terminate_srv, args=(srv,))
            td.start()


def terminate_srv(srv):
    srv.shutdown()


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 12345
    srv = socketserver.UDPServer((HOST, PORT), MyHandle)
    srv.serve_forever()
