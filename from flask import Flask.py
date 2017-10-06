from __future__ import print_function
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Ciara!'

if __name__ == '__main__':
    app.run(debug=True) #run the development web server
