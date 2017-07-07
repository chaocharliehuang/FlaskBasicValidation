from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['post'])
def process():
    name = request.form['name']
    email = request.form['email']
    if len(name) < 1:
        flash('Name cannot be empty!')
    else:
        flash('Success! Your name is {}'.format(name))
    
    if len(email) < 1:
        flash('Email cannot be blank!')
    elif not EMAIL_REGEX.match(email):
        flash('Invalid email address!')
    else:
        flash('Success!')
    
    return redirect('/')

app.run(debug=True)