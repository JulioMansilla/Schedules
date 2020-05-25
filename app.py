from flask import Flask

#special python variable with the name of the module
app=Flask(__name__)


#define routes
@app.route("/")
def hello():
    return "<h1>??????</h1>"
