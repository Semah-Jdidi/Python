from flask import Flask , render_template , request , redirect , session

app = Flask(__name__)
app.secret_key = '1q8FTOEtih'

@app.route('/')
def root():
    return render_template('home.html')

@app.route('/process' , methods=['POST'])
def create_account():
    session['username'] = request.form['name']
    session['location'] = request.form['city']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def show_results():
    return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)