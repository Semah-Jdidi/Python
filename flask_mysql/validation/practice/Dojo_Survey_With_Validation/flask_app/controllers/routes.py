from flask_app.models import survey
from flask_app import app
from flask import render_template , redirect , request , session

@app.route('/')
def root():
    return render_template('home.html')

@app.route('/process' , methods=['POST'])
def create_account():
    if not survey.Survey.validation(request.form):
        return redirect('/')
    data = request.form
    survey.Survey.create_survey(data)
    return redirect('/result')

@app.route('/result')
def show_results():
    dojo = survey.Survey.display_survey()
    return render_template('result.html' , dojos = dojo)