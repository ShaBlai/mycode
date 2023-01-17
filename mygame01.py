#!/usr/bin/python3

#!/usr/bin/python3

import random
import sys
import time
import webbrowser

from art import *

print("🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕")               
tprint("Escape The Haunted Pizza Parlor")
print("🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕")


def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    
  
    print('''
    
    ========
    Commands:
      go [direction]
      get [item]
    ''', )
    
def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom + ": " + rooms[currentRoom]['description'])
    # print what the player is carrying
    print('This is your inventory at the moment: ', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item']['name'] + ': ' + rooms[currentRoom]['item']['description'])
    print(f'You have made {moves} moves')
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

            'Pizza Lobby' : {
                  'north' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item' : {'name' : 'Lottery Ticket','description':'This could change my life! Or leave me stuck in this place...'},
                  'description' : 'The abandoned entrance/lobby of what used to be my favorite pizza place...reeks of old cardboard and deliciously bad cholesterol',
                  'west' : 'Pizza Parlor'
                },

            'Kitchen' : {
                  'north' : 'Back-Alley',
                  'south' : 'Pizza Lobby',
                  'item' : {'name': 'Old-School Boombox', 'description': 'I used to jam out with these...talk about nostalgia!'},
                  'description' : 'Dirty Dishes, Old Ingredients, and a block of Blue Cheese that used to be Mozzarella? Smells great...'
                },
                                     
            'Dining Room' : {
                  'west': 'Pizza Lobby',
                  'south' : 'Garden',
                  'item' : {'name': 'Magical Pepperoni', 'description': 'A pepperoni inscribed with the following.."Return me home, and so shall thee"'},
                  'description': 'Where all the customers used to eat delicious pizzas...where has everyone gone?'
                },
            
            'Back-Alley' : {
                'south' : 'Kitchen',
                'item' : {'name':'Raggedy Cassette Tape', 'description': 'A weathered cassette tape...artist is unreadable, but the album is "Whenever You Need Somebody"'},
                'description': 'Your typical sketchy, "do not want to hang out here long" type of area'
                },
            
            'Pizza Parlor' : {
                'east' : 'Pizza Lobby',
                'item' : {'name': 'Incomplete Pizza', 'description': 'A pizza that radiates magical energy, however is missing a special topping...'},
                'description' : 'A lone glowing pizza sits upon a golden pedestal...marble pillars and picasso artwork line the walls'                               
            }    
                              
         }

# start the player in the Hall
currentRoom = 'Pizza Lobby'

showInstructions()

gamerun = True

#counter for the moves made
moves = 0



# breaking this while loop means the game is over
while gamerun:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            moves += 1
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')


    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom]:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
            moves += 1
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
            
   
    #if for when the player gets a lottery ticket and wins the jackpot to escape
    if ('lottery ticket' in inventory):
        
        #creating the outcomes for the lottery ticket if the user decides to pick it up
        mega_millions_outcomes = {"Option 1: ":"$Bajillion Jackpot!", "Option 2: ": "$3.50", "Option 3: ": "$50.00", "Option 4:" : "$10,000"}
        mega_millions_chance = (random.choice(list(mega_millions_outcomes.values())))
                        
        print('Would you like to scratch off this lottery ticket? Could get something good...')
        userinput3 = input(" Yes or No: ".lower())
        if userinput3 ==('yes'):
            if mega_millions_chance =="$Bajillion Jackpot!":
                tprint("You have ESCAPED!! THANK YOU LOTTERY!!")
                break
            elif mega_millions_chance !="$Bajillion Jackpot!":
                print(f"You have won {mega_millions_chance}!")
                inventory.remove('lottery ticket')
      
    ## If a player enters a room with pizza in it
    if (currentRoom == 'Pizza Parlor' and 'incomplete pizza'  and 'magical pepperoni' in inventory):
        print('The Magical Pepperoni glows intensely the closer it is to the pizza...')
        print('Would you like reunite the magical pepperoni to the pizza?')
        userinput2 = input(" Yes or No :".lower())
        
        if userinput2 == ('yes'):
            print("The Pizza begins to glow brighter and brighter...your body begins to feel light as a feather and everything becomes dark...")
            tprint("..................................")
            print("You wake up in the back of a horse-drawn carriage...realizing you just had the weirdest nightmare ever")
            tprint("...Hey you, you're finally awake")
            tprint("A new adventure begins!")
            break
        elif userinput2 ==('no'):
            print("You decided not to reunite the magical pepperoni...the pizza became angry and tranformed into a giant Monster!")
            print("Which murdered you...great")
            tprint("YOU DIED")
            break 
        
      ## If a player enters a room with pizza in it
    if (currentRoom == 'Dining Room'  and 'incomplete pizza'  and 'magical pepperoni' in inventory):
        print('The Magical Pepperoni glows intensely the closer it is to the pizza...')
        print('Would you like reunite the magical pepperoni to the pizza?')
        userinput2 = input(" Yes or No :".lower())
        
        if userinput2 == ('yes'):
            print("The Pizza begins to glow brighter and brighter...your body begins to feel light as a feather and everything becomes dark...")
            print("..................................")
            print("You wake up in the back of a horse-drawn carriage...realizing you just had the weirdest nightmare ever")
            tprint("...Hey you, you're finally awake")
            tprint("A new adventure begins!")
            break
        elif userinput2 ==('no'):
            print("You decided not to reunite the magical pepperoni...the pizza became angry and tranformed into a giant Monster!")
            print("Which murdered you...great")
            tprint("YOU DIED")
            break          
            
   
    #generates the music webpage if they play the song
    if ('old-school boombox' and 'raggedy cassette tape' in inventory):
       
       #url for the 
        ra_video_url = {"Never gonna give you up:": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}
         
        print ('Put the tape in the boombox to hear some jams? "Whenever you need somebody" is dull, but still readable on the cassette...')
        print('Definitely not giving this cassette up...Play it? ')
        userinput = input(" Yes or No: ".lower())
       
        if userinput ==("yes"):
            tprint("Now playing")
            tprint("Rick Astley's 1987 Hit")
            tprint("Never gonna give you up")
            webbrowser.open_new_tab(random.choice(list(ra_video_url.values())))
            inventory.remove('old-school boombox')
            inventory.remove('raggedy cassette tape')
        elif userinput == ("no"):
            print("That's okay, nows not the time to rock. We are trapped in a haunted pizza parlor!")    
                                
           