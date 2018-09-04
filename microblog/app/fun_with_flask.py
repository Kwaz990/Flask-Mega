from flask import Flask
from flask import render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
#import app
#from forms import LoginForm
from app.forms import LoginForm

####This is the view function
app = Flask(__name__)
app.config['SECRET_KEY'] ='you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'



db = SQLAlchemy(app)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kwasi'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in New York City!!!'
        },
        {
            'author': {'username': 'Blacknimbus'},
            'body': 'I love crypto'
         }
     ]
    return render_template('index.html',title ='Home', user = user, posts = posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user{}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title = 'Sign In', form =form)


#    return '''
#<html>
#    <head>
#        <title> Home Page - Microblog </title>
#    </head>
#    <body>
#        <h1> Greetings, '''  + user['username'] + '''!</h1>
#    </body>
#</html>'''



if __name__ == '__main__':
    app.run('127.0.0.1', debug = True)
