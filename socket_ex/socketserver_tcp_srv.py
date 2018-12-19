# coding=utf-8
"""
@version: 2017/12/14 014
@author: Suen
@contact: sunzh95@hotmail.com
@file: socketserver_tcp_srv
@time: 10:59
@note:  ??
"""
#

import threading

__metaclass__ = type

import socketserver

class MyHandle(socketserver.StreamRequestHandler):
    def handle(self):
        # rfile, wfile / request
        while True:
            # data = self.request.recv(1024)
            data = self.rfile.readline()
            print("Data recevied from client: {}".format(data.decode('utf-8').strip('\n')))
            # self.request.sendall(data)
            self.wfile.write(data)
            if data in (b'Bye', b'Bye\n'):
                break
        print('server terminated')
        td = threading.Thread(target=terminate_srv, args=(srv,))
        td.start()


def terminate_srv(srv):
    srv.shutdown()


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 12345
    srv = socketserver.TCPServer((HOST, PORT), MyHandle)
    srv.serve_forever()
