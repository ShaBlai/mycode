#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 1009!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()
    #print(pokeapi["sprites"]["front_default"])
    #print(pokeapi)
    
    name = pokeapi["name"]
    print(name)
   
    for x in pokeapi["moves"]:
        x = x["move"]["name"]
        print(x)

main()
