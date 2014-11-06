from flask import Flask
from flask import request
from os import listdir
from os.path import isfile, join
import sys

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

@app.route('/ListFiles')
def list_files():
    onlyfiles = [f for f in listdir("./uploads/") if isfile(join("./uploads/",f))]
    listToReturn = ""
    for i in onlyfiles:
        listToReturn = listToReturn + i + "\n"
    return listToReturn

@app.route('/Euler1')
def euler1():
    x = 1;
    sum = 0;
    for x in range(1000):
        if (x%3 == 0 or x%5 == 0): sum += x;
    newSum = str(sum)
    return newSum

@app.route('/Euler2')
def euler2():
    a = 0;  #inicialization of varibales
    b = 1;

    sum_fib = 0

    while True:
        a, b = b, a+b
        if b >= 4000000:
            break
        if (b%2 == 0):
            sum_fib+=b

    newSumFib = str(sum_fib)
    return newSumFib
