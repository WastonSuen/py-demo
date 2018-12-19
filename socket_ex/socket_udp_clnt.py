# coding=utf-8
"""
@version: 2017/12/12 012
@author: Suen
@contact: sunzh95@hotmail.com
@file: socket_udp_clnt
@time: 15:12
@note:  ??
"""
#

import socket

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 12345
    clnt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        data = 'Hello'
        while data:
            clnt.sendto(data.encode('utf-8'), (HOST, PORT))
            if data in (b'Bye', b'Bye\n'):
                break
            data, addr = clnt.recvfrom(1024)
            # if not data:
            #     data, addr = clnt.recvfrom(1024)
            print("Received From Server: {}".format(data.decode('utf-8')))
            data = input("Please give a message to server:\n")

    except Exception:
        print('Error')
    finally:
        clnt.close()
