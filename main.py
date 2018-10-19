from flask import Flask,render_template,request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

#route for get
@app.route('/')
def signup():
    return render_template('user-signup.html')

#functions to validate length, spaces, empty field, and '@' and '.' in email
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

#route for post
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
    succes_condition = 0    #counter if no error =0 - return succes.html

    #validate username
    if use_pass(username) == False:
        username= ''
        username_error = main_msg.format('username')
        succes_condition+=1

    #validate password
    if use_pass(password) == False:
        password_error = main_msg.format('password')
        succes_condition+=1

    #validate verify-password
    if password != verify:
        verify_error = verify_msg 
        print(verify_error)
        succes_condition+=1

    #validate email
    if eml(email) == False:
        email = ''
        email_error = main_msg.format('email')
    #if any error= render user-signup.html with errors else render succes.html
    if succes_condition > 0:
        return render_template('user-signup.html', username=username, username_error=username_error, 
        password='', password_error=password_error, 
        verify='', verify_error=verify_error,
        email=email, email_error=email_error)
    else:
        return render_template('succes.html', username=username)

app.run()
