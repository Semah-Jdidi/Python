from flask import Flask , render_template


app = Flask(__name__)   


@app.route('/')   

@app.route('/play')
def play():
    return render_template('index.html' , num = 3 , color= "#5585b5")

@app.route('/play/<int:num>')
def display(num):
    return render_template('index.html', num=num , color= "#5585b5")

@app.route('/play/<int:num>/<string:color>')
def color(num, color):
    return render_template('index.html', num = num, color=color)


if __name__=="__main__":      
    app.run(debug=True)  