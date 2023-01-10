#!/usr/bin/env python3


def main():
    #creating the first list of network eqpt
    list1 = ["cisco_nxos", "artista_oes", "cisco_ios"]

    #prints the entire list
    print(list1)
    #prints the second item in the list
    print(list1[1])
    
    #creates a second list of juniper
    list2 =["Juniper"]
    
    #iterates juniper and adds to list1
    list1.extend(list2)


    print(list1) 

    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    list1.append(list3)

    
    print(list1)


    print (list1[4])


    print(list1[4][0])

    #creating the animal list
    animalList = ["Fox","Fly","Ant","Bee","Cod"]

    print(animalList)




main()    

