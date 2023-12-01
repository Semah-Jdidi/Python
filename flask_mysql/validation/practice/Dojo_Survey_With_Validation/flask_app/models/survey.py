from flask_app.config.mysqlconnection import DB , connectToMySQL
from flask import flash

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def create_survey(cls, data):
        query = 'INSERT INTO dojo_surveys(name, location, language, comment, created_at, updated_at) VALUES(%(name)s , %(location)s , %(language)s , %(comment)s , NOW() , NOW() );'
        result = connectToMySQL(DB).query_db(query, data)
        return result
    
    @classmethod
    def display_survey(cls):
        query = 'SELECT * FROM dojo_surveys;'
        result = connectToMySQL(DB).query_db(query)
        return result
    
    @staticmethod
    def validation(survey):
        is_valid = True
        if len(survey['name']) < 3 :
            is_valid = False 
            flash('Name must be at least 3 characters!')
        if len(survey['location']) < 1 :
            is_valid = False 
            flash('You must choose a location!')
        if len(survey['language']) < 1 :
            is_valid = False 
            flash('You must choose a language')
        if len(survey['comment']) < 3 :
            is_valid = False 
            flash('Comment must be more than 3 characters')
        return is_valid