#!/usr/bin/env python3
import requests
import random
from flask import request
from flask import render_template
from flask import redirect
from flask import Flask
from flask import url_for

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)




    


@app.route("/", methods=["POST", "GET"])
def startpage():
        
    #changes categories randomly depending on what number was selected
    URL = (f"https://opentdb.com/api.php?amount=3")
    
    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL)

    #adds the json data to questions    
    myquestions = data.json()
        
    #parse through the json and return the questions/answers       
    question1 = myquestions['results'][1]['question']
    answer1 = myquestions['results'][1]['correct_answer']
    incorrect1 =myquestions['results'][1]['incorrect_answers']
    
    #creating and shuffling the correct/incorrect answers       
    bankofstuff1 = [answer1] 
    bankofstuff1.extend(incorrect1)
    random.shuffle(bankofstuff1)
   
    #rendering the template with Jinja and assigning the variables within the HTML     
    return render_template("landing.html", question1 = question1, answerbank1 = bankofstuff1)

    # if request.method =="POST":
    #     if request.form["answer"] == answer1:
    #         print("YOU ARE RIGHT")
    #     else:
    #         print("YOU ARE WRONG")
            
            
@app.route("/", methods =["POST"])
def formsubmit():

    if request.method =="POST":
        if request.form["answer"] == answer1:
            print("YOU ARE RIGHT")
        else:
            print("YOU ARE WRONG")

                    
  
@app.route("/correct")
def correct():
    return "CORRECT-A-MUNDO my friend!"  

# @app.route("/one")
# def one():
#     return "Hello world!"

# @app.route("/two/<adjective>")
# def two(adjective):
#     return f"I hope today is {adjective}"

# @app.route("/three", methods = ["POST", "GET"])    
# def three():
#     return "Changes and deletions only, please!"

# @app.route("/four")
# def four():
#     return redirect("/one")    
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
    