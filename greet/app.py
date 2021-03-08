from flask import Flask

app = Flask(__name__)


@app.route("/welcome/")
def say_welcome():
    #Return welcome greeting
    return "welcome"

@app.route("/welcome/home")
def say_welcomehome():
    #returns welcome home greeting
    return "welcome home"

@app.route("/welcome/back")
def say_welcomeback():
    #returns welcome back greeting
    return "welcome back"