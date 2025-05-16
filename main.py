from flask import Flask,render_template

app=Flask(__name__) ## creates an instance of flask which will be wsgi application


@app.route("/")
def welcome():
    return "<html><H1>Welcome to the Home page</H1></html>"

@app.route("/index")
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)