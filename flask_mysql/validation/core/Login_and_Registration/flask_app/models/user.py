from flask_app.config.mysqlconnection import connectToMySQL, DB
from flask_app import app
from flask_bcrypt import Bcrypt
import re
from flask import flash

bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

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
    def registration(cls, data):
        encrypted_password = bcrypt.generate_password_hash(data['password'])
        data = dict(data)
        data['password'] = encrypted_password
        query = 'INSERT INTO users(first_name, last_name, email, password) VALUES(%(first_name)s , %(last_name)s , %(email)s , %(password)s);'
        result = connectToMySQL(DB).query_db(query, data)
        return result
    
    @classmethod
    def get_by_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        result = connectToMySQL(DB).query_db(query, data)
        if result:
            return cls(result[0])
        return False
    
    @staticmethod
    def register_validation(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        if len(data['first_name']) <= 3:
            flash('First Name Must Be Longer Than 3 Characters!','register')
            is_valid = False
        if len(data['last_name']) <= 3:
            flash('Last Name Must Be Longer Than 3 Characters!','register')
            is_valid = False
        if len(data['password']) < 8:
            flash('Password Must Be At Least 8 Characters!','register')
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash('Passwords Does Not Match!','register')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash('Invalid Email Adress!','register')
            is_valid = False
        if user_in_db:
            flash('A User With This Email Already Exists!','register')
            is_valid = False
        return is_valid
    
    @staticmethod
    def login_validation(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        if not EMAIL_REGEX.match(data['email']):
            flash('Invalid Email Adress!','login')
            is_valid = False
        if not user_in_db:
            flash('User Does Not Exist','login')
            is_valid = False
        elif not bcrypt.check_password_hash(user_in_db.password, data['password']):
            flash('Password Is Incorrect','login')
            is_valid = False
        return is_valid