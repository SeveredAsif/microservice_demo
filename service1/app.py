from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello from Service 1!")

@app.route('/call-service2')
def call_service2():
    try:
        #response = requests.get("http://service2:5001/")
        response = requests.get("https://microservice-demo-2new.onrender.com/")
        return jsonify(message="(CI CHECK PUSH) Service 1 received: " + response.json()['message'])
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
