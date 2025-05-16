from flask import Flask

app=Flask(__name__) ## creates an instance of flask which will be wsgi application


@app.route("/")
def welcome():
    return "Welcome to my web page."

@app.route("/index")
def index():
    return "Welcome to my index page."

if __name__=="__main__":
    app.run(debug=True)