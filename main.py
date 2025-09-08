from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route("/")
def index():

    return "Hello World! This is my home page!"

if __name__ == "__main__":
    app.run(debug=True)