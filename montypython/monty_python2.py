#!/usr/bin/env python3

round = 0
answer = " "

while round < 3 and (answer !="Brian" and answer !="Shrubbery"):
    round = round +1
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess--> ")
    answer = answer.capitalize()


    if answer == "Brian":
        print ("Correct")
    elif answer =="Shrubbery":
        print ("You gave the super secret answer")
    elif round ==3:
        print ("Sorry, the answer was Brian")
        break
    else:
        print("Sorry, try again")


