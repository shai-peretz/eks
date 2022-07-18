from flask import Flask, request
import requests
import os
app = Flask(__name__)

#port = os.environ['PORT']

@app.route("/")
def general():
    return "OK"

@app.route("/hello")
def hello():
    return "<h1>Hello World</h1>"

@app.route("/host_ip")
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

@app.route("/client")
def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = "<h2>ip</h2>" + ip_address \
                     + "<h2>city</h2>" + response.get("city") \
                     + "<h2>region</h2>" + response.get("region") \
                     + "<h2>country</h2>" + response.get("country_name")
    return location_data

@app.route("/health")
def health():
    return "service is healthy"


'''
FLASK MAIN
'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)