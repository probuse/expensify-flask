from flask import render_template
from expensify import app

@app.route('/')
def home():
    return render_template('home.html')

