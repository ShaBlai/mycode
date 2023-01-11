#!/usr/bin/env python3

#create a quiz to where a user tries to guess my favorite 90s rock band and play the music associated

import webbrowser


#create guesses and answer
rockGuesses = 0
answer = " "


alcUrl = "https://www.youtube.com/watch?v=ODTv9Lt5WYs"
metUrl = "https://www.youtube.com/watch?v=E0ozmU9cJDg"
pjUrl = "https://www.youtube.com/watch?v=RgStt2i_pSk"


#establish the while loop

#if rockguesses are less than three keep going
while rockGuesses < 3 and answer !="alice in chains" and answer !="metallica" and answer!="pearl jam":
    
    #incrementing rockguesses
    rockGuesses = rockGuesses+1
    #prompt user with question
    print("What are my three favorite 90s grunge/rock bands?")
    #gather user input
    answerMusic= input("Please enter your guess--> ")
    #lowercase user input
    answerMusic = answerMusic.lower() 

    #if the answer is alice in chains, execute and open the music URL
    if (answerMusic =="alice in chains"):
        print("Congrats, you know your stuff! Time to jam out, I STAYYYY AWAYYYYY")
        webbrowser.open_new_tab(alcUrl)
        break
   #if the answer is metallica, execute and open the music URL
    if (answerMusic == "metallica"):
        print("Correct, time to ROCK OUT! My other favorites are Alice In chains and Pearl Jam")
        webbrowser.open_new_tab(metUrl)
        break
    #if the answer is pearl jam, execute and open the music URL    
    if (answerMusic == "pearl jam"):
        print("Correct, time to listen to Eddie Vedder! My other favorites are Metallica and Alice In Chains")
        webbrowser.open_new_tab(pjUrl)
        break
    
    #output if 2 guesses have been made
    elif rockGuesses==2:
        print("You have one more guess...so much pressure (Hint: My friend ALICE talks about METAL with PEARL)")    
    #output if user runs out of guesses
    elif rockGuesses == 3:
        print("Sorry my friend...the answers were Alice In Chains, Metallica, or Pearl Jam'!")
        
    else:
        print("That is incorrect, please enter another Artist/Band!")        
    

        