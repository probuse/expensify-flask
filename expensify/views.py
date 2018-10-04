from functools import wraps
from flask import render_template, request, redirect, url_for, flash
from expensify import app

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Please Login to continue')
            return redirect(url_for('login'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] == 'etwin@himself.com' and request.form['password'] == 'etwin':
            return redirect(url_for('home'))
        error = 'Invalid email or Password'
    return render_template('login.html', error=error)

