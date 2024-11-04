## integrate HTML with Flask 
## HTTP verb like GEET & POST

import flask 
from flask import Flask,url_for, redirect, render_template, request

app = Flask(__name__) 

@app.route('/')
def welcome_message():
    return render_template('index.html')

## Result checker HTML page 
@app.route('/submit',methods=['POST','GET'])
def submit():
    avg = 0 
    res=""
    if request.method=='POST':
        maths_marks =float(request.form['science'])
        science_marks = float(request.form['maths'])
        avg = (maths_marks+science_marks)/2

    if avg>=33:
        res = 'success'
    else:
        res = 'fail'
    
    return redirect(url_for(res,my_score=avg))

@app.route('/success/<float:my_score>')
def success(my_score):
    return render_template('success.html',score=my_score)

@app.route('/fail/<float:my_score>')
def fail(my_score):
    return render_template('fail.html',score=my_score)

if __name__ == '__main__' :
    app.run(debug=True)