from flask import Flask,render_template,request

app=Flask(__name__) ## creates an instance of flask which will be wsgi application


@app.route("/")
def welcome():
    return "<html><H1>Welcome to the Home page</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name} !'
    return render_template('forms.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        comment=request.form['comment']
        return f"Hello {name}!<br>Your comment is : {comment}"
    return render_template('forms.html')

if __name__=="__main__":
    app.run(debug=True)