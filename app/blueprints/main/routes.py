from contextlib import redirect_stderr
from app import app
from flask import render_template

@app.route('/home')
def home ():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/online')
def online():
    return render_template('online.html')

@app.route('/inperson')
def inperson():
    return render_template('inperson.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')
            
