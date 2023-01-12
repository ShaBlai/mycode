#!/usr/bin/env python3

#parse the keystone log and return the number of failed attempts

loginfail = 0 #counter for the fails

#open the keystone file log
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r")

#read the lines in the file
keystone_file_lines = keystone_file.readlines()

for line in keystone_file_lines:
    if "- - - - -] Authorization failed." in line:
        loginfail +=1
print("The number of failed login attempts is", loginfail)

keystone_file.close()
