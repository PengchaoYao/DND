

import socket
import time
import getopt
import sys
import struct
import os

    
if __name__ == "__main__":    
    dstport = 502   
    dstip ="192.168.0.10"     
    addr = (dstip,dstport)
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(addr)


    sendstr3="\x00\x00\x00\x00\x00\x06\x01\x05\x02\x0a\xff\x00"
    sock.send(sendstr3)

    sendstr4="\x00\x00\x00\x00\x00\x06\x01\x05\x02\x0a\x00\x00"
    sock.send(sendstr4)



    
   
    
    sock.close()       

            
