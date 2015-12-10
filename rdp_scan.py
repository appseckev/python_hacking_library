#!/usr/bin/env python
#Scans a range and outputs a list of targets with the Remote Desktop port open :)

import sys
from scapy import *
conf.verb=0

if len(sys.argv) != 2:
    print "Usage: ./rdp_scan.py <target>"
    print "Where <target> is a range like 192.168.1.0/24"
    sys.exit(1)

target=sys.argv[1]

p=IP(dst=target)/TCP(dport=3389, flags="S")
ans,unans=sr(p, timeout=9)

for a in ans:
    if a[1].flags == 2:
        print a[1].src


