import socket

s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ('182.20.1.1',9999)
s.bind(addr)

while True:
    print('a')
    data=s.recv(1024)
    print(data)