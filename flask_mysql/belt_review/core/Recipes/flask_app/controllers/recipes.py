from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User
from flask import render_template , redirect , request , session

@app.route('/recipes')
def new_recipe():
    if not 'logged_user' in session:
        return redirect('/')
    data = {
        "id" : session['logged_user']
    }
    logged_user = User.get_by_id(data)
    return render_template('new_recipe.html', logged_user = logged_user)

@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    if not 'logged_user' in session:
        return redirect('/')
    if not Recipe.recipe_validation(request.form):
        return redirect('/recipes')
    Recipe.create_recipe(request.form)
    return redirect('/dashboard')

@app.route('/recipes/<int:id>')
def display_recipe(id):
    recipe = Recipe.get_by_id({'id':id})
    logged_user = User.get_by_id({'id': session['logged_user']})
    return render_template('display_recipes.html', user = logged_user, recipe = recipe)

@app.route('/recipes/<int:id>/update')
def update_recipe(id):
    recipe = Recipe.get_by_id({'id': id})
    if not 'logged_user' in session:
        return redirect('/')
    elif recipe.user.id != session['logged_user']:
        return redirect('/dashboard')
    return render_template('update_recipe.html', recipe = recipe)

@app.route('/recipes/update', methods=['POST'])
def update():
    Recipe.update_recipe(request.form)
    return redirect('/dashboard')

@app.route('/recipes/<int:id>/delete')
def delete(id):
    data = {'id' : id}
    recipe = Recipe.get_by_id(data)
    if recipe.user.id == session['logged_user']:
        Recipe.delete_recipe(data)
    return redirect('/dashboard')