## Builiding URL dynamically 
## Variable rules and URL building 

import flask 
from flask import Flask, redirect, url_for 

app = Flask(__name__)

@app.route('/')
def welcome_message():
    return "welcome to my website"

@app.route('/success/<int:score>')
def success(score):
    return "<html><body><div>This person has passed the exam with the score of : </div></body></html>"

@app.route('/fail/<int:score>')
def fail(score):
    return "This person has failed the exam with the score of : " + str(score)

#Result checker 
@app.route('/result/<int:marks>')
def result_check(marks):
    my_result = ""
    if marks>=35:
        result = "success"
    else : 
        result = "fail"
    return redirect(url_for(result,score=marks))


if __name__ == '__main__':
    app.run(debug=True)