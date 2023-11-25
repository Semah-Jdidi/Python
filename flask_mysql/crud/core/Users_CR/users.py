from mysqlconnection import DB , connectToMySQL

class user:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def create_user(cls , data):
        query = 'INSERT INTO users(first_name , last_name , email) Values(%(first_name)s , %(last_name)s , %(email)s);'
        results = connectToMySQL(DB).query_db(query , data)
        return results
    
    @classmethod
    def get_users(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL(DB).query_db(query)
        
        users = []
        for row in results:
            users.append(cls(row))
            
        return users