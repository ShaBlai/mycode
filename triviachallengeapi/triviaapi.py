#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import random


#sets a random number between 1 & 31
category = random.randint(1, 31)
#changes categories randomly depending on what number was selected
URL= (f"https://opentdb.com/api.php?amount=3&category={category}")



def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL)

    #adds the json data to questions    
    myquestions = data.json()
    print(myquestions)
     
    #parse through the json and return the questions/answers       
    question1 = myquestions['results'][0]['question']
    answer1 = myquestions['results'][0]['correct_answer']
    question2 = myquestions['results'][1]['question']
    answer2 = myquestions['results'][1]['correct_answer']
    question3 = myquestions['results'][2]['question']
    answer3 = myquestions['results'][2]['correct_answer']
    
    #prompt user with question
    print(question1)
    #ask for input
    userinput1 = input("What is the correct answer? \n")
    #logic for if the user gets the questions right
    if userinput1 == answer1:
        print("Nice job, you are correct! \n")
    else:
        print(f"That is incorrect, the correct answer is {answer1} \n")
    
    print(question2)
    userinput2 = input("What is the correct answer? \n")
    if userinput2 == answer2:
        print("Nice job, you are correct! \n")
    else:
        print(f"That is incorrect, the correct answer is {answer2} \n")
    
    print(question3)
    userinput3 = input("What is the correct answer? \n")
    if userinput3 == answer3:
        print("Nice job, you are correct! \n")
    else:
        print(f"That is incorrect, the correct answer is {answer3} \n")   
    
    
    
   # print(question1)
   # print(answer1)
   # print(question2)
   # print(answer2)
   # print(question3)
   # print(answer3)
    

if __name__ == "__main__":
    main()
