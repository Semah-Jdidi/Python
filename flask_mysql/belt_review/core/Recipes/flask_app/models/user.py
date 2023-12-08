from flask_app.config.mysqlconnection import connectToMySQL , DB
from flask_app import app
from flask_bcrypt import Bcrypt
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

bcrypt = Bcrypt(app)


class User:
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def create_user(cls, data):
        encypted_password = bcrypt.generate_password_hash(data['password'])
        data = dict(data)
        data['password'] = encypted_password
        query = 'INSERT INTO users(first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);'
        result = connectToMySQL(DB).query_db(query, data)
        return result
    
    @classmethod
    def get_by_id(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s'
        result = connectToMySQL(DB).query_db(query, data)
        user = None
        if result:
            user = cls(result[0])
        return user
    
    @classmethod
    def get_by_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        result = connectToMySQL(DB).query_db(query, data)
        if result:
            return cls(result[0])
        return False
    
    @staticmethod
    def validate_registration(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        if len(data['first_name']) <= 2:
            flash("First Name Must Be Longer Than 2 Characters!", "registration")
            is_valid = False
        if len(data['last_name']) <= 2:
            flash("Last Name Must Be Longer Than 2 Characters!", "registration")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid Email Adress!", "registration")
            is_valid = False
        if len(data['password']) < 8:
            flash("Password Must Be At Least 8 Characters!", "registration")
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash("Passwords Don't Match!", "registration")
            is_valid = False
        if user_in_db:
            flash("A User With This Email Adress Already Exists!", "registration")
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_login(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid Email Adress!", "login")
            is_valid = False
        if not user_in_db:
            flash("User Does Not Exist!", "login")
            is_valid = False
        elif not bcrypt.check_password_hash(user_in_db.password, data['password']):
            flash("Incorrect Password!", "login")
            is_valid = False
        return is_valid