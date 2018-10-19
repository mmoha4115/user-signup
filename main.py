from flask import Flask,render_template,request, redirect
import os
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def signup():
    return render_template('user-signup.html')


def length(field):
    if field > 3 and field < 20:
        return True
    return False

def spaces(field):
    space = ' '
    if space in field:
        return False
    return True

def empty(field):
    emp = ''
    if field == emp:
        return False
    return True

def at_check(email):
    at = '@'
    dot = '.'
    if at in email and dot in email:
        return True
    return False

def use_pass(field):
    error = empty(field)
    if error == False:
        return False
    error = length(field)
    if error == False:
        return False
    error = spaces(field)
    if error == False:
        return False
    return True


def eml(field):
    error = 
    


@app.route('/', methods=['POST'])
def signedup():
    username= request.form['username']
    password= request.form['password']
    verify= request.form['verify']
    email= request.form['email']





    return render_template('user-signup.html', username=username,password=password,verify=verify,email=email)


app.run()
