from flask_app.config.mysqlconnection import DB , connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def create_email(cls, data):
        query = 'INSERT INTO emails(email, created_at, updated_at) VALUES(%(email)s , NOW() , NOW());'
        result = connectToMySQL(DB).query_db(query, data)
        return result
    
    @classmethod
    def display_email(cls):
        query = 'SELECT * FROM emails'
        result = connectToMySQL(DB).query_db(query)
        return result
    
    @staticmethod
    def validation(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            is_valid = False
            flash('Invalid Email Adress!')
        return is_valid