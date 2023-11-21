from flask import Flask, render_template, redirect, request, session



app = Flask(__name__)  
app.secret_key='5D36C'

@app.route('/')          
def counter():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":      
    app.run(debug=True)    