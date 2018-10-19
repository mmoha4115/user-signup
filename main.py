from flask import Flask,render_template,request, redirect
import os
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def signup():
    return render_template('user-signup.html')


def length(field):
    if len(field) > 3 and len(field) < 20:
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

def atdot_check(email):
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
    error = length(field)
    if error == False:
        return False
    error = spaces(field)
    if error == False:
        return False
    error = atdot_check(field)
    if error == False:
        return False
    return True

    


@app.route('/', methods=['POST'])
def signedup():
    username= request.form['username']
    password= request.form['password']
    verify= request.form['verify']
    email= request.form['email']

    main_msg = "That's not a valid {0}"
    verify_msg = "Passwords don't match"

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if use_pass(username) == False:
        username= ''
        username_error = main_msg.format('username')
        password = ''
        verify = password

    if use_pass(password) == False:
        password= ''
        password_error = main_msg.format('password')
        
    if password != verify:
        print(verify_error)
        verify_error = verify_msg
        password = ''
    
    if eml(email) == False:
        email = ''
        email_error = main_msg.format('email')
    verify = password
    
    return render_template('user-signup.html', username=username, username_error=username_error, 
    password=password, password_error=password_error, 
    verify=verify, verify_error=verify_error,
    email=email, email_error=email_error)

app.run()
