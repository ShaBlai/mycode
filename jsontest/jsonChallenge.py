#!/usr/bin/env python3


import requests


IPURL = "http://ip.jsontest.com/"
TIMEURL= "http://date.jsontest.com/"
VALIDURL = "http://validate.jsontest.com/"

def main():
    
    #Part A getting the time
    resp = requests.get(TIMEURL)
    #assigning variable to json
    mytime = resp.json()    
    #pulling the date and time from json
    mydate = mytime["date"]
    mytime = mytime["time"]
       
    print(mydate)
    print(mytime)
    
    
    
    #Part B getting IP address
    #gets the IP address JSON
    resp = requests.get(IPURL)
    
    #assigns the request to JSON Var
    myip = resp.json()
    #pulling the IP key
    myip = myip["ip"]
    #printing output
    print(myip)
    
    ## PART C
    ## read a list of hosts out of a flat file
    with open("/home/student/mycode/jsontest/myservers.txt") as myfile:
        mysvrs = myfile.readlines()

    ## PART D
    # test data to validate as legal json
    # when a POST json= is replaced by the KEY "json"
    # the key "json" is mapped to a VALUE of the json to test
    # because the test item is a string, we can include whitespaces
    # format for requests to validate.testjson.com is...
    # data={"json": "json you want to validate as str"}
    jsonToTest = {}
    jsonToTest["time"] = mytime
    jsonToTest["ip"] = myip
    jsonToTest["mysvrs"] = mysvrs

    mydata = {}
    mydata["json"] = str(jsonToTest)

    ## PART E
    # use requests library to send an HTTP POST
    resp = requests.post(VALIDURL, data=mydata)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)

    # JUST display the value of "validate"
    print(f"Is your JSON valid? {respjson['validate']}")

if __name__ == "__main__":
    main()    #Part C Read in list of servers
    
    
    
 