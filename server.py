from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['post'])
def process():
    name = request.form['name']
    if len(name) < 1:
        flash('Name cannot be empty!')
    else:
        flash('Success! Your name is {}'.format(name))
    return redirect('/')

app.run(debug=True)