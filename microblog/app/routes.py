from flask import Flask
from flask import render_template
from forms import LoginForm

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kwasi'}
    return render_template('index.html', title = 'Home', user=user)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Sign In', form= form)




if __name__ == '__main__':
    app.run('127.0.0.1', debug = True)
