#!/usr/bin/env python3

with open ("dnsservers.txt", "r") as dnsfile:
    #indent to keep the file open because of the "with open"
    #loop across that txt to get the data
    for svr in dnsfile:
        svr = svr.rstrip("\n") #remove newline char if exists
                               #would exist on all but last line   
                                    
        #if the string svr ends with an "org"                       
        if svr.endswith("org"):
            with open("org-domain.txt", "a") as srvfile: # a is for append
                srvfile.write(svr + "\n")
                
        #if the string svr ends with an "com"        
        elif svr.endswith("com"):
            with open("com-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")
                
                
                
                