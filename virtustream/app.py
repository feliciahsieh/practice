#!/usr/bin/python3

from flask import Flask

fibonacci = __import__('fibonacciWebSvc').fibonacci


app = Flask(__name__)

@app.route('/')
def index():
#    return "Hello, World!\n"
    return str(fibonacci(5))

if __name__ == '__main__':
    app.run(debug=True)
