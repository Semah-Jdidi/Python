from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask import render_template , redirect , request , session

@app.route('/')
def root():
    if 'logged_user' in session:
        return redirect('/dashboard')
    return render_template('login_registration.html')

@app.route('/registration', methods=['POST'])
def registration():
    if User.validate_registration(request.form):
        User.create_user(request.form)
        return redirect('/')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    if User.validate_login(request.form):
        user = User.get_by_email(request.form)
        session['logged_user'] = user.id
        return redirect('/dashboard')
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if not 'logged_user' in session:
        return redirect('/')
    logged_user = User.get_by_id({'id': session['logged_user']})
    recipes = Recipe.get_all()
    return render_template('dashboard.html', user = logged_user, recipes = recipes)

@app.route('/logout')
def logout ():
    session.clear()
    return redirect('/')