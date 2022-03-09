#!/usr/bin/env python3

dnsfile = open("dnsservers.txt", "r")
dnslist = dnsfile.readline()

for svr in dnslist:
    print(svr, end="")

dnsfile.close()
