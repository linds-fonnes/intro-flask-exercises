from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add_nums():
    #returns sum of a & b
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    sum = add(a,b)
    return str(sum)

@app.route("/sub")
def sub_nums():
    #returns difference of a & b
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    diff = sub(a,b)
    return str(diff)

@app.route("/mult")
def mult_nums():
    #returns product of a & b
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    product = mult(a,b)
    return str(product)

@app.route("/div")
def div_nums():
    #returns remainder of a & b
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    remainder = div(a,b)
    return str(remainder)

math_operators = {
     "add" : add,
     "sub" : sub,
     "mult": mult,
     "div" : div
 }   

@app.route("/math/<operation>")
def math(operation):
    #returns answer based on operation chosen
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    value = math_operators[operation](a,b)
    return str(value)