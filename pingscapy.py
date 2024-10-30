#!/usr/bin/python3

from scapy.all import *
conf.verb = 0

for ip in range(1, 255):
        iprange = "37.59.174.%s" %ip
        pIP = IP(dst=iprange)
        pacote = pIP/ICMP()
        resp, noresp = sr(pacote,timeout=1)
        print(resp.show())
        for resposta in resp:
                print(resposta[1][IP].src)
