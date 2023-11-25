from flask import Flask , render_template , redirect , request
from users import user

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/process' , methods=['POST'])
def form():
    data = request.form
    user.create_user(data)
    return redirect('/display')

@app.route('/display')
def display_users():
    all_users = user.get_users()
    return render_template('results.html', users = all_users)

if __name__ == '__main__':
    app.run(debug=True)