#!/usr/bin/env python3


#open the file in read mode
dnsfile = open("dnsservers.txt", "r")

#create a list of lines
dnslist = dnsfile.readlines()


#loop over the lines
for svr in dnslist:
    #print and end without a newline
    print(svr, end="") # the line we read ALREADY contains a \n (newline)

#close the file we 
dnsfile.close()    
