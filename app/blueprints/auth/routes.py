from . import bp as app
from app.blueprints.main.models import User 
from app import db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from app.blueprints.auth.forms import SignupForm, LoginForm 

@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if request.method == 'GET':
            return render_template('login.html', form = form)

    if form.validate_on_submit():
        try:
            if form.validate_on_submit():
                email = form.email.data 
                password = form.password.data
                print(email)
                

                user = User.query.filter_by(email= email).first()

                if user is None:
                    flash('There is not a profile with that email.', 'danger')
                elif not user.check_my_password(password):
                    flash('The password was incorrect.', 'danger')
                else:
                    flash('Log in successful', 'success')
                    login_user(user)
                    return redirect(url_for('home'))
        except Exception as err:
            raise Exception(err)

    return render_template('login.html' , form = form)

@app.route('/register', methods=['GET', 'POST'])
def register():

    form = SignupForm()

    if request.method == 'GET':
        return render_template('register.html', form = form)
    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            password = form.password.data
            confirm_password = form.confirm_password.data

            check_user = User.query.filter_by(email=email).first()

            if check_user is not None:
                flash('A user with this email already exists.', 'danger')

            elif password != confirm_password:
                flash('The passwords do not match', 'danger')

            new_user = User(email=email, first_name=first_name, last_name=last_name, password='')
            new_user.hash_my_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('User registered successfully', 'success')
            return redirect(url_for('auth.login'))
    except Exception as err:
        raise Exception(err)

    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    flash('Logged out', 'success')
    return redirect(url_for('auth.login'))

@login_manager.unauthorized_handler
def unauthorized_handler():
    flash("Please log in to access this page.", 'danger')
    return redirect(url_for('auth.login'))