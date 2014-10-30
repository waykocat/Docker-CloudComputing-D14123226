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
