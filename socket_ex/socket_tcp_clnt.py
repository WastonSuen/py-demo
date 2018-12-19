# coding=utf-8
"""
@version: 2017/12/12 012
@author: Suen
@contact: sunzh95@hotmail.com
@file: socket_tcp_clnt
@time: 14:50
@note:  ??
"""
#
import socket

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 12345
    clnt = socket.socket()
    try:
        data = 'Hello!'
        clnt.connect((HOST, PORT))
        while data:
            data += '\n'
            clnt.sendall(data.encode('utf-8'))
            data = clnt.recv(1024)
            print("Received From Server: {}".format(data.decode('utf-8').strip('\n')))
            if data in (b'Bye', b'Bye\n'):
                break
            data = input("Please give a message to server:\n")
    except socket.error as e:
        print(e)
    except Exception:
        print('Unknow Error')
    finally:
        clnt.close()
