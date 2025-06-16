#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'
@app.route("/print/<string:parameter>")
def print_parameter(parameter):
    print(parameter)
    return f'{parameter}'
@app.route("/count/<int:parameter>")
def count(parameter):
    count=f""
    for i in range(parameter):
        count+=f"{i}\n"
    return count
@app.route("/math/<int:parameter1>/<string:operation>/<int:parameter2>")
def math(parameter1,parameter2,operation):
    if operation=="+":
        return str(parameter1+parameter2)
    elif operation=="-":
        return str(parameter1-parameter2)
    elif operation=="*":
        return str(parameter1*parameter2)
    elif operation=="div":
        return str(parameter1/parameter2)
    elif operation=="%":
        return str(parameter1%parameter2)
    return 'error'
if __name__ == '__main__':
    app.run(port=5555, debug=True)
