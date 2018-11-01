#!/usr/bin/python3

from flask import Flask

fibonacci = __import__('fibonacciWebSvc').fibonacci


app = Flask(__name__)

@app.route('/')
def index():
    return("Welcome to the world of Fibonacci numbers\n")

@app.route('/<n>')
def runProgram(n):
    return str(fibonacci(n)) + "\n"

if __name__ == '__main__':
    app.run(debug=True)
