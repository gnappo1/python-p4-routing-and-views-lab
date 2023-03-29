#!/usr/bin/env python3
import re
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)
    return f"{parameter}"

@app.route("/count/<int:parameter>")
def count(parameter):
    page = ""
    for num in range(parameter):
        page += f"{num}\n"
    return page

@app.route("/math/<input>")
def math(input):
    op = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        'div': lambda x, y: x / y,
        '*': lambda x, y: x * y,
        '%': lambda x, y: x % y
    }

    operation_regex = re.compile('div|[+\\-*%]')
    number_regex = re.compile('\\d+')

    operand = operation_regex.findall(input)
    numbers = number_regex.findall(input)

    if operand and len(numbers) > 1:
        return f"{op[operand[0]](int(numbers[0]), int(numbers[1]))}"
    return "Touble - Houston help!"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
