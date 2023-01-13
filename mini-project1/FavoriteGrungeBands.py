#!/usr/bin/env python3

#create a quiz to where a user tries to guess my favorite 90s rock band and play the music associated

import webbrowser
import random






def main():
    #establish the while loop
    #if rockguesses are less than three keep going
    #create guesses and answer
    rockGuesses = 0
    answer = " "

    #Switched to a dictionary, named the videos associated
    alcVideoURL = {"I Stay Away": "https://www.youtube.com/watch?v=ODTv9Lt5WYs", "Nutshell": "https://www.youtube.com/watch?v=9EKi2E9dVY8", "Down in a Hole": "https://www.youtube.com/watch?v=E17hqs4Un-k"}
    metVideoURL = {"Master of Puppets": "https://www.youtube.com/watch?v=E0ozmU9cJDg", "Fuel": "https://www.youtube.com/watch?v=0JJPqA-KwOw", "Enter Sandman": "https://www.youtube.com/watch?v=CD-E-LDc384"}
    pjVideoURL = {"Black": "https://www.youtube.com/watch?v=RgStt2i_pSk", "Even Flow": "https://www.youtube.com/watch?v=CxKWTzr-k6s","Jeremy": "https://www.youtube.com/watch?v=JNZezhUkOSk"}
    
    while rockGuesses < 3 and answer !="alice in chains" and answer !="metallica" and answer!="pearl jam":
    
    
        #incrementing rockguesses
        rockGuesses = rockGuesses+1
        #prompt user with question
        print("What is one of my favorite 90s grunge/rock bands? There are three correct answers.")
        #gather user input
        answerMusic= input("Please enter your guess--> ")
         #lowercase user input
        answerMusic = answerMusic.lower() 

        #if the answer is alice in chains, execute and open the random music URL
        if (answerMusic =="alice in chains"):
            print("Congrats, you know your stuff! Time to jam out, I STAYYYY AWAYYYYY")
            #uses the web browser to open the URL after a random one from the list has been selected
            webbrowser.open_new_tab(random.choice(list(alcVideoURL.values())))
            break
    
       #if the answer is metallica, execute and open the random music URL
        if (answerMusic == "metallica"):
            print("Correct, time to ROCK OUT! My other favorites are Alice In chains and Pearl Jam")
            #uses the web browser to open the URL after a random one from the list has been selected
            webbrowser.open_new_tab(random.choice(list(metVideoURL.values())))
            break
    
        #if the answer is pearl jam, execute and open the random music URL    
        if (answerMusic == "pearl jam"):
            print("Correct, time to listen to Eddie Vedder! My other favorites are Metallica and Alice In Chains")
            #uses the web browser to open the URL after a random one from the list has been selected
            webbrowser.open_new_tab(random.choice(list(pjVideoURL.values())))
            break
    
        #output if 2 guesses have been made
        elif rockGuesses == 2:
            print("You have one more guess...so much pressure (Hint: My friend ALICE talks about METAL with PEARL)")    
        #output if user runs out of guesses
        elif rockGuesses == 3:
            print("Sorry my friend...the answers were Alice In Chains, Metallica, or Pearl Jam'!")
    #for incorrect answers response        
    else:
        print("That is incorrect, please enter another Artist/Band!")        
        
#the if name is main
if __name__ == "__main__":
    main()        
    

        
