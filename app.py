from flask import Flask
app = Flask(__name__)

@app.route("/nagli-secret-endpoint.txt")
def hello():
    return "shockwave poc - nagli"
