from flask_app.config.mysqlconnection import connectToMySQL , DB
from flask_app import app
from flask_app.models import user
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made_on = data['date_made_on']
        self.made_under_30 = data['made_under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
    
    @classmethod
    def create_recipe(cls, data):
        query = 'INSERT INTO recipes(name, description, instructions, date_made_on, made_under_30, user_id) VALUES(%(name)s, %(description)s, %(instructions)s, %(date_made_on)s, %(made_under_30)s, %(user_id)s);'
        result = connectToMySQL(DB).query_db(query, data)
        return result
    
    @classmethod
    def update_recipe(cls, data):
        query = 'UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made_on = %(date_made_on)s, made_under_30 = %(made_under_30)s WHERE id = %(id)s;'
        result = connectToMySQL(DB).query_db(query, data)
        return result
    
    @classmethod
    def delete_recipe(cls, data):
        query = 'DELETE FROM recipes WHERE id = %(id)s;'
        result = connectToMySQL(DB).query_db(query, data)
        return result
    
    @classmethod
    def get_by_id(cls, data):
        query = 'SELECT * FROM recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;'
        result = connectToMySQL(DB).query_db(query, data)
        recipe = None
        if result:
            recipe = cls(result[0])
            user_data = {
                'id' : result[0]['users.id'],
                'first_name' : result[0]['first_name'],
                'last_name' : result[0]['last_name'],
                'email' : result[0]['email'],
                'password' : result[0]['password'],
                'created_at' : result[0]['users.created_at'],
                'updated_at' : result[0]['users.updated_at']
            }
            recipe.user = user.User(user_data)
        return recipe
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;'
        result = connectToMySQL(DB).query_db(query)
        recipes = []
        if result:
            for row in result:
                recipe = cls(row)
                user_data = {
                    'id' : row['users.id'],
                    'first_name' : row['first_name'],
                    'last_name' : row['last_name'],
                    'email' : row['email'],
                    'password' : row['password'],
                    'created_at' : row['users.created_at'],
                    'updated_at' : row['users.updated_at']
                }
                recipe.user = user.User(user_data)
                recipes.append(recipe)
        return recipes
    
    @staticmethod
    def recipe_validation(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("Recipe Name Must Be At Least 3 Characters!","recipe")
            is_valid = False
        if len(data['description']) < 3:
            flash("Description Must Be At Least 3 Characters Long!","recipe")
            is_valid = False
        if len(data['instructions']) < 3:
            flash("Instructions Must Be At Least 3 Characters Long!","recipe")
            is_valid = False
        if data['date_made_on'] == "":
            flash("Date Must Be Filled!","recipe")
            is_valid = False
        return is_valid