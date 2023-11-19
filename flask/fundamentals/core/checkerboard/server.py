from flask import Flask , render_template


app = Flask(__name__)    


@app.route('/')
def root():
    return render_template('index.html' , column=8 , row= 8)


@app.route('/<int:row>')
def rows(row):
    return render_template('index.html' , column=8 , row=row)

@app.route('/<int:row>/<int:column>')
def rows_and_columns(column,row):
    return render_template('index.html' , column=column , row=row)


if __name__=="__main__":      
    app.run(debug=True)    