from flask import render_template
from flask import flash
from flask import redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Kevin'}
    posts = [
        {
            'author' : {'username' : 'John'},
            'body' : 'Beautiful day in Portland!'
        },
        {
            'author' : {'username' : 'Susan'},
            'body' : 'The Avengers Movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {usr}, remember_me={rem}'.format(
            usr=form.username.data,
            rem=form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)