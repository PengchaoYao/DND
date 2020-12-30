#! /usr/bin/env python
# coding: utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('182.20.1.1', 8000))

while True:
    data, addr = s.recvfrom(1024)
    print(data[:500])