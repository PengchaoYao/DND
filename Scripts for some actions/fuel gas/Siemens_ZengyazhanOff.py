

import socket
import time
import getopt
import sys
import struct
import os

    
if __name__ == "__main__":    
    dstport = 503   
    dstip ="192.168.0.110"     
    addr = (dstip,dstport)
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(addr)



    sendstr1="\x00\x00\x00\x00\x00\x06\x01\x06\x00\x18\x00\x01"
    sock.send(sendstr1)

    sendstr2="\x00\x00\x00\x00\x00\x06\x01\x06\x00\x18\x00\x00"
    sock.send(sendstr2)



    
   
    
    sock.close()       

            
