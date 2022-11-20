from flask import Flask
import os

app = Flask(__name__)

@app.route("/", methods =['GET'])
def hello():
    return "Your First ever app!! :-)"

if __name__ == "__main__":
    app.run()
