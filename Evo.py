from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def main():
    return "Hello Word"

@app.route('/login')
def login():
    pass

@app.route()
def register('/register'):
    pass

@app.route('user/<username>',methods = ['GET','POST','PUT','DELETE'])
def user():
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass
    elif request.method == "PUT":
        pass
    elif request.method == "DELETE":
        pass

@app.route('departnment/<department>',methods = ['GET','POST','PUT','DELETE'])
def department():
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass
    elif request.method == "PUT":
        pass
    elif request.method == "DELETE":
        pass

@app.route('position/<position>',methods = ['GET','POST','PUT','DELETE'])
def position():
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass
    elif request.method == "PUT":
        pass
    elif request.method == "DELETE":
        pass

if __name__ == '__main__':
    app.run()
