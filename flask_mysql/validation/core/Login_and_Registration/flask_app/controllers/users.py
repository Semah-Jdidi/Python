from flask_app import app
from flask_app.models import user
from flask import render_template, redirect, request, session, flash

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def create_account():
    if user.User.register_validation(request.form):
        user.User.registration(request.form)
        return redirect('/success')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    if user.User.login_validation(request.form):
        session['logged_user'] = request.form['email']
        return redirect('/success')
    return redirect('/')

@app.route('/success')
def success():
    if not 'logged_user' in session:
        return redirect('/')
    logged_user = user.User.get_by_email({'email': session['logged_user']})
    return render_template('success.html' , logged_user = logged_user )

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')