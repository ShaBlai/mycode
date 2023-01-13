#!/usr/bin/env python3

#opening our dracula for reading

with open("dracula.txt", "r") as draculabook:
        draculabook = draculabook.readlines()
        count =0
with open("vampytimes.txt", "w") as vampy:
    for item in draculabook:
        if "vampire" in item.lower():
            count += 1
            print(item)
            vampy.write(item)
    print(count)        
          
            
            
            
        