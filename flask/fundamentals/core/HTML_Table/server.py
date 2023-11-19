from flask import Flask , render_template


app = Flask(__name__)    


heading = ['First Name' , 'Last Name' , 'Full Name']


users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi', 'full_name' : 'Michael Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin', 'full_name' : 'John Supspin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen', 'full_name' : 'Mark Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel', 'full_name' : 'KB Tonel'} 
]


@app.route('/')
def root():
    return render_template('index.html', heading = heading , users = users)






if __name__=="__main__":      
    app.run(debug=True)  
    