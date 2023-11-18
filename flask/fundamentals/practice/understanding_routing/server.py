from flask import Flask


app = Flask(__name__)

    
@app.route('/')          
def hello_world():
    return 'Hello World!'

@app.route('/dojo')          
def dojo():
    return 'dojo'

@app.route('/say/<string:name>')          
def say(name):
    print(name)
    return f'Hello {name}'

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num, name):
    return name * num


if __name__=="__main__":      
    app.run(debug=True)    