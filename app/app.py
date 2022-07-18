from flask import Flask, request
import requests
import os
app = Flask(__name__)

port = os.environ['PORT']

@app.route("/")
def general():
    return "OK"

@app.route("/hello")
def hello():
    return "<h1>Hello World</h1>"

@app.route("/host_ip")
def index():
    server_name = request.environ['SERVER_NAME']
    server_ip = requests.get('http://ifconfig.io')
    return "Host: " + str(server_name) + "\n" + "Server info: " + str(server_ip.text)

@app.route("/health")
def health():
    return "service is healthy"


'''
FLASK MAIN
'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port), debug=True)