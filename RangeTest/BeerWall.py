#!/usr/bin/env python 3

#generate the countdown for bottles song


def main():
    
    #initiate the count    
    count = 99
    #create the range for it to be generated
    for x in range (0, 99):
        print(f"{count} bottles of beer on the wall!")
        print(f"{count} bottles of beer! Take one down, pass it around")
        count = count -1
        print(f"{count} bottles of beer on the wall!")
        
        if count == 0:
            print("You've drank all the beer, my friend. Here's some tylenol")
            break
      

main()        
