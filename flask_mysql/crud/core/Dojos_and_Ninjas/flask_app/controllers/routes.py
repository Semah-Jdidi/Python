from flask import render_template , redirect , request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    all_dojos = Dojo.display_dojos()
    return render_template('index.html' , dojos = all_dojos)

@app.route('/create', methods = ['POST'])
def create_dojo():
    data = request.form
    Dojo.create_dojos(data)
    return redirect('/')

@app.route('/dojo/<int:id>')
def display_all(id):
    data = {'id' : id}
    dojo = Dojo.join_all(data)
    return render_template('ninjas_with_dojos.html', dojo = dojo)



@app.route('/ninja')
def add_ninja():
    dojo = Dojo.display_dojos()
    return render_template('/ninja.html' , dojos = dojo)

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    data = request.form
    Ninja.create_ninjas(data)
    return redirect('/')