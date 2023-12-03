from flask import render_template, redirect, request, flash
from flask_app import app
from flask_app.models import email

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def create():
    if not email.Email.validation(request.form):
        return redirect('/')
    email.Email.create_email(request.form)
    return redirect('/display')

@app.route('/display')
def display_emails():
    data = email.Email.display_email()
    return render_template('display.html', emails = data)