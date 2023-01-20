#!/usr/bin/env python3
import requests
import random
import html
import time
from flask import request
from flask import render_template
from flask import redirect
from flask import Flask
from flask import url_for
from flask import session

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)



#global variables to be used throughout
QUESTION1 = ""
CORRECT_ANSWER1 = ""
BANKOFSTUFF1 =[]
USER_SCORE = 0
RANDOJOKE = ""


@app.route("/", methods=["GET"])
def startpage():
    global QUESTION1, CORRECT_ANSWER1, BANKOFSTUFF1
        
    #changes categories randomly depending on what number was selected
    URL = (f"https://opentdb.com/api.php?amount=3")
    
    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL)

    #adds the json data to questions    
    myquestions = data.json()
        
    #parse through the json and return the questions/answers       
    QUESTION1 = html.unescape(myquestions['results'][1]['question'])
    CORRECT_ANSWER1 = html.unescape(myquestions['results'][1]['correct_answer'])
    INCORRECT1 = html.unescape(myquestions['results'][1]['incorrect_answers'])
    
    #creating and shuffling the correct/incorrect answers       
    BANKOFSTUFF1 = [CORRECT_ANSWER1] 
    BANKOFSTUFF1.extend(INCORRECT1)
    random.shuffle(BANKOFSTUFF1)
    print(CORRECT_ANSWER1)
    #rendering the template with Jinja and assigning the variables within the HTML     
    return render_template("landing.html", question1 = QUESTION1, answerbank1 = BANKOFSTUFF1, userscore= USER_SCORE)

#creating the logic for when the answer is submitted from HTML
@app.route("/submit", methods=["POST"])
def submit():
    #importing global correct answers and scores
    global CORRECT_ANSWER1, USER_SCORE
    print(request.form.get("answer"))
    #logic that verifies if the user selects the right answer
    #if user gets right, adds their points and keeps the game going
    if request.form.get("answer").lower() == CORRECT_ANSWER1.lower():
        USER_SCORE = USER_SCORE + 500
        return redirect("/")
    #if the user gets it wrong, erases their points and redirects to the wrong page
    else:
        USER_SCORE = 0
        return redirect("/wrong")
    
#creating the page and logic for the wrong page
#attempting to add a joke api if you got it wrong
@app.route("/wrong", methods = ["GET"])
def wrongo():
    global RANDOJOKE
    
    #api for the random joke to make users who got it wrong feel better 
    JOKEURL= "https://official-joke-api.appspot.com/random_joke"
        
    #getting the joke JSON
    jokedata = requests.get(JOKEURL)
    
    #assigning jsons to joke
    myjokes = jokedata.json()
    
    #parsing out the JSON
    jokeprompt = html.unescape(myjokes["setup"])
    jokepunchline = html.unescape(myjokes["punchline"])
    #returns the wrong answer HTML page and assigned the jokes to the jinja variables
    return render_template("wrong.html", jokeprompt = jokeprompt, jokepunchline = jokepunchline )  
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
    