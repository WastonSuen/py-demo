# coding=utf-8
"""
@version: 2017/12/12 012
@author: Suen
@contact: sunzh95@hotmail.com
@file: guibackup_srv
@time: 15:57
@note:  ??
"""
#
from tkinter import *
from tkinter.ttk import *

__metaclass__ = type

import os
import time
import struct
import pickle
import socket
import codecs
import threading

BAK_PATH = r'D:\workspace\backup'
SERVER_RUN_FLAG = True


def send_echo(client, res):
    if res:
        client.send(b'success')
    else:
        client.send(b'failure')


def mk_path(filepath):
    file_dir = os.path.dirname(filepath)
    if not os.path.exists(file_dir):
        os.mkdir(file_dir)


def get_compressed_size(client):
    fmt_str = 'Q'
    compressed_size_headsize = struct.calcsize(fmt_str)
    size_data = recv_unit_file(client, compressed_size_headsize)
    compressed_size, = struct.unpack(fmt_str, size_data)
    return compressed_size


def recv_file(client, infos_len, file_name, compress):
    filepath = os.path.join(BAK_PATH, file_name)
    mk_path(filepath)

    if compress:
        infos_len = get_compressed_size(client)
        filepath = ''.join([os.path.splitext(filepath)[0], '.tar.gz'])

    with codecs.open(filepath, 'ab+') as f:
        while infos_len:
            if infos_len >= 1024:
                f.write(recv_unit_file(client, 1024))
                infos_len -= 1024
            elif infos_len > 0:
                f.write(recv_unit_file(client, infos_len))
                break
            else:
                break
    print("Succeed reveiving {}".format(file_name))
    return True


def get_files_info(client):
    fmt_str = 'Q?'
    headsize = struct.calcsize(fmt_str)
    infos_data = recv_unit_file(client, headsize)
    infos_len, compress = struct.unpack(fmt_str, infos_data)
    data = pickle.loads(recv_file_data(client, infos_len))
    print("Received file infos: {}".format(data))
    return data, compress


def recv_file_data(client, infos_len):
    data = b''
    while infos_len:
        if infos_len >= 1024:
            data += recv_unit_file(client, 1024)
            infos_len -= 1024
        elif infos_len > 0:
            data += recv_unit_file(client, infos_len)
            break
        else:
            break
    return data


def process_connetion(client):
    files_info, compress = get_files_info(client)
    for size, file_name in files_info:
        print("Starting receiving {} of {}".format(size, file_name))
        res = recv_file(client, size, file_name, compress)
        send_echo(client, res)
    print("All Done\n")
    client.close()


def recv_unit_file(client, size):
    """
    receive every data-bytes by block, no data no return 
    :param client: 
    :param headsize: 
    :return: 
    """
    while True:
        try:
            data = client.recv(size)
        except:
            time.sleep(1)
        else:
            break
    return data


def start(host, port):
    if not os.path.exists(BAK_PATH):
        os.mkdir(BAK_PATH)
    srv = socket.socket()
    srv.settimeout(1)
    srv.bind((host, port))
    srv.listen(1)
    mylock.acquire()
    while SERVER_RUN_FLAG:
        mylock.release()
        try:
            clnt, addr = srv.accept()
        except:
            pass
        else:
            print("Connected to {}".format(addr))
            td = threading.Thread(target=process_connetion, args=(clnt,))
            td.start()
        finally:
            time.sleep(1)
            mylock.acquire()
    srv.close()


class MyFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        self.root = root
        self.grid()
        self.local_ip = '127.0.0.1'
        self.serv_ports = [12345, 12343, 12344]
        self.init_components()

    def init_components(self):
        proj_name = Label(self, text="Backup Server")
        proj_name.grid(columnspan=2)

        srv_ip_label = Label(self, text='ip addr')
        srv_ip_label.grid(row=1)
        self.serv_ip = Combobox(self, values=self.get_ipaddr())
        self.serv_ip.set(self.local_ip)
        self.serv_ip.grid(row=1, column=1)

        srv_port_label = Label(self, text='port')
        srv_port_label.grid(row=2)
        self.serv_port = Combobox(self, values=self.serv_ports)
        self.serv_port.set(self.serv_ports[0])
        self.serv_port.grid(row=2, column=1)

        self.start_srv_btn = Button(self, text='Start', command=self.start_server)
        self.start_srv_btn.grid(row=3)

        self.exit_srv_btn = Button(self, text='Exit', command=self.exit_server)
        self.exit_srv_btn.grid(row=3, column=1)

    def get_ipaddr(self):
        host_name = socket.gethostname()
        info = socket.gethostbyname_ex(host_name)[2]
        assert isinstance(info, list)
        info.append(self.local_ip)

    def start_server(self):
        host, port = self.serv_ip.get(), int(self.serv_port.get())
        print("Starting Server on: {}:{}".format(host, port))
        td = threading.Thread(target=start, args=(host, port))
        # self.start_srv_btn.state(['disabled', ])
        td.start()

    def exit_server(self):
        self.root.destroy()


class MyTk(Tk):
    def destroy(self):
        """
        when destroy window, stop acccepting connections from client, 
        buy still process the requests already received.
        :return: 
        """
        global SERVER_RUN_FLAG
        mylock.acquire()
        if SERVER_RUN_FLAG:
            SERVER_RUN_FLAG = False
        mylock.release()
        Tk.destroy(self)


if __name__ == '__main__':
    mylock = threading.Lock()
    root = MyTk()
    root.title = 'Backup Server'
    root.resizable(False, False)
    app = MyFrame(root)
    app.mainloop()
