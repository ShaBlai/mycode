#!/usr/bin/env python3



def main():
    """runtime function"""


    ##creating the dictionaries
    switch = {"hostname": "sw", "ip": "10.0.1.1", "version" : "1.2", "vendor": "cisco"}

    ##displaythe dictionary
    print(switch)

    ## proove that switch is a dictionairy
    print(type(switch))


    print( switch["hostname"] )
    print( switch["ip"] )

    print ( switch["lynx"] )


if __name__ == "__main__":
    main()        


