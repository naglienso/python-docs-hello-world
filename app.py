from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "nagli or m0chan-takeover"
