from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(message="Holaa desde Flask :)")

@app.route("/health")
def health():
    return jsonify(status="ok")


