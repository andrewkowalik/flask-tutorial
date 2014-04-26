from flask import render_template, flash, redirect
from app import app
from forms import LoginForm
from flask.ext.security import login_required


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'nickname': 'Miguel'}
    return render_template("index.html",
        title = 'Home',
        user =user)

# @app.route('/login', methods = ['GET', 'POST'])
# def login():
    # form = LoginForm()
    # if form.validate_on_submit():
    #     flash('Login requsted for ' + form.username.data)
    #     return redirect('/index')
    # return render_template('login.html',
    #     title = 'Sign In',
    #     form = form)