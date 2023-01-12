#!/usr/bin/env python3


with open("dnsservers.txt", "r") as dnsfile:
    #indent to keep the dns file object open
    #create the list of names
    dnslist = dnsfile.readlines()
    #loop through the lines
    for svr in dnslist:
        #print and end without a newline
        print(svr, end="")