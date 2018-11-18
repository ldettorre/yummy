import os
from flask import Flask, render_template,redirect,request

app = Flask(__name__)

@app.route("/")
def test():
    return "This is an app test"

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))