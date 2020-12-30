#!/usr/bin/env python
# coding: utf-8



from scapy.all import *
import threading
import sys
import time 

time_start=time.time() 
def dealwith():
    print ('开始抓包')
    # 下面的iface是电脑网卡的名称 count是捕获报文的数目
    dpkt = sniff(iface="以太网 2")  # 抓包 # prn=lambda x: x.show(),
    # pkts = sniff(prn=lambda x : x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}"))
    print ('抓包成功')
 
    wrpcap("D://demo.pcap", dpkt)
    print ('所抓的包已经保存')
 
    pcks = rdpcap('D://demo.pcap')
    print ('开始解析pcap包')
 
    # 输出重定向  讲在控制台的输出重定向到 txt文本文件中
    output = sys.stdout
    outputfile = open('D://capture.txt', 'w')
    sys.stdout = outputfile
 
    zArp = 0
    zIcmp = 0
    ipNum = set()
 
    for p in pcks:
        status1 = p.payload.name  # 可能是ARP的报文
        status2 = p.payload.payload.name  # 可能是TCP报文 也可能是ICMP的报文
 
        # p.show() 输出报文， 在符合的情况下
        if status1 == 'IP':
            ipNum.add(p.payload.src)  # 将ip报文的源地址，和目的地址存在set集合里面（set去重）
            ipNum.add(p.payload.dst)
            p.show()
            print ('s')
        else:
            if status1 == 'ARP':
                p.show()
                print ('d')
                zArp += 1
 
            if status2 == 'ICMP':
                p.show()
                print ('dd')
                zIcmp += 1
 
    print ('IP：' + str(len(ipNum)) + ' ARP：' + str(zArp) + ' ICMP：' + str(zIcmp)) # 报文数量的输出
 
    outputfile.close()
    sys.stdout = output  # 恢复到控制台输出
 
    print ('输出结束')
    print (dpkt)
 
dealwith() # 运行报文捕获函数




time_end=time.time()
print('totally cost',time_end-time_start)


# In[ ]:




