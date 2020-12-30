#! /usr/bin/env python
# coding: utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('182.20.1.1', 20000))
s.listen()

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    print(data[:500])