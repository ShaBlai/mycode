#!/usr/bin/env python3

#create the file link/opening

#userinput =input("What is the name of the file you would like to load?")

with open("vlanconfig.cfg", "r") as configfile:
    #readlines() creates a list by reading the target
    #file line by line
    configlist = configfile.readlines()
    configlen = len(str(configfile.readlines()))
    
print(configlist, configlen)    