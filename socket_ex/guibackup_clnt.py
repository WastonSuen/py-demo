# coding=utf-8
"""
@version: 2017/12/12 012
@author: Suen
@contact: sunzh95@hotmail.com
@file: guibackup_clnt
@time: 18:04
@note:  ??
"""
#

__metaclass__ = type

import tkinter
from tkinter import ttk

import os
import struct
import pickle
import socket
import codecs
import threading
import tarfile, tempfile


def get_files_infos(src):
    """
    :param src:source root dir 
    :return: 
    """
    if not src or not os.path.exists(src):
        return [], []
    src_info = os.walk(src)  # [(path,[children_dir_path],[files_name]),...]

    files_infos = []
    files_paths = []
    root_dir = os.path.split(src)[-1]
    for path, child_dir, files in src_info:
        for file_name in files:
            file_full_path = os.path.join(path, file_name)
            files_paths.append(file_full_path)

            file_size = os.stat(file_full_path).st_size
            relative_path = os.path.join(root_dir, file_full_path[len(src) + 1:])
            files_infos.append((file_size, relative_path))
    return files_infos, files_paths


def send_files_infos(client, files_infos, compress):
    fmt_str = 'Q?'
    infos_bytes = pickle.dumps(files_infos)

    infos_bytes_len = len(infos_bytes)
    infos_bytes_len_pack = struct.pack(fmt_str, infos_bytes_len, compress)
    client.sendall(infos_bytes_len_pack)
    client.sendall(infos_bytes)


def send_files(client, file_path, compress):
    if compress:
        f = tempfile.NamedTemporaryFile()
        with tarfile.open(mode="w|gz", fileobj=f) as tar_file:
            tar_file.add(file_path)
        f.seek(0)
        file_size = os.stat(f.name).st_size
        file_size_bytes = struct.pack('Q', file_size)
        client.sendall(file_size_bytes)
    else:
        f = codecs.open(file_path, 'rb')
    try:
        data = f.read(1024)
        while data:
            print("Sending: {}".format(file_path))
            client.sendall(data)
            data = f.read(1024)
    except:
        pass
    finally:
        f.close()


def get_bak_info(client, size=7):
    """
    get the backup echo from server
    :param client: 
    :param size: 
    :return: 
    """
    data = client.recv(size)
    print(data.decode('utf-8'))


def start(host, port, src, compress):
    if not os.path.exists(src):
        raise ValueError('FILEPATH')
    clnt = socket.socket()
    clnt.connect((host, port))
    file_infos, file_paths = get_files_infos(src)
    send_files_infos(clnt, file_infos, compress)
    for fp in file_paths:
        send_files(clnt, fp, compress)
        get_bak_info(clnt)
    clnt.close()


class MyFrame(ttk.Frame):
    def __init__(self, root):
        super(MyFrame, self).__init__()

        self.root = root
        self.grid()
        self.remote_ip = '127.0.0.1'
        self.remote_ip_var = tkinter.StringVar()
        self.remote_ports = [12345, 12343, 12344]
        self.remote_ports_var = tkinter.IntVar()
        self.back_src_var = tkinter.StringVar()
        self.compress_var = tkinter.BooleanVar()
        self.init_components()

    def init_components(self):
        proj_name = tkinter.Label(self, text="Backup Client")
        proj_name.grid(columnspan=2)

        srv_ip_label = tkinter.Label(self, text='ip addr: ')
        srv_ip_label.grid(row=1)
        self.serv_ip = tkinter.Entry(self, textvariable=self.remote_ip_var)
        self.remote_ip_var.set(self.remote_ip)
        self.serv_ip.grid(row=1, column=1)

        srv_port_label = tkinter.Label(self, text='port: ')
        srv_port_label.grid(row=2)
        self.serv_port = tkinter.Entry(self, textvariable=self.remote_ports_var)
        self.remote_ports_var.set(self.remote_ports[0])
        self.serv_port.grid(row=2, column=1)

        src_label = tkinter.Label(self, text='src to backup: ')
        src_label.grid(row=3)
        self.back_src = tkinter.Entry(self, textvariable=self.back_src_var)
        self.back_src_var.set(os.path.abspath(r'D:\workspace\scripts\Oct'))
        self.back_src.grid(row=3, column=1)

        tar_label = tkinter.Label(self, text='tar?')
        tar_label.grid(row=4)
        self.compress_on = tkinter.Checkbutton(self, text='True', variable=self.compress_var, onvalue=1, offvalue=0)
        self.compress_on.grid(row=4, column=1)

        self.start_srv_btn = tkinter.Button(self, text='Start', command=self.start_send)
        self.start_srv_btn.grid(row=5)

        self.exit_srv_btn = tkinter.Button(self, text='Exit', command=self.root.destroy)
        self.exit_srv_btn.grid(row=5, column=1)

    def start_send(self):
        host, port = self.remote_ip_var.get(), int(self.remote_ports_var.get())
        src = self.back_src_var.get()
        compress = bool(self.compress_var.get())
        print("Starting Backup Client on: {}:{}".format(host, port))
        # threadings to release the windown while backups
        td = threading.Thread(target=start, args=(host, port, src, compress))
        # self.start_srv_btn.state(['disabled', ])
        td.start()

    def exit_server(self):
        pass


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title = 'Backup Server'
    root.resizable(False, False)
    app = MyFrame(root)
    app.mainloop()
