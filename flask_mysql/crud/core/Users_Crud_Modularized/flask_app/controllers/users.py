from flask_app import app
from flask import render_template , redirect , request
from flask_app.models.user import user

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/process' , methods=['POST'])
def form():
    data = request.form
    user.create_user(data)
    return redirect('/display')

@app.route('/display')
def display_users():
    all_users = user.get_users()
    return render_template('results.html', users = all_users)