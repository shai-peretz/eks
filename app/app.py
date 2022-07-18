from flask import Flask, request
import requests
import os
app = Flask(__name__)
port = os.getenv("PORT", "2323")
host = os.getenv("HOST", "0.0.0.0")
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
def print_location():
    response = get_location()
    location_data = "<h2>Ip</h2>" + response.get("ip") \
                     + "<h2>City</h2>" + response.get("city") \
                     + "<h2>Region</h2>" + response.get("region") \
                     + "<h2>Country</h2>" + response.get("country_name")
    return location_data

@app.route("/geo")
def get_location():
    ip_address = get_ip()
    return requests.get(f'https://ipapi.co/{ip_address}/json/').json()


@app.route("/health")
def health():
    return "service is healthy"

'''
FLASK MAIN
'''
if __name__ == '__main__':
    app.run(host=host, port=int(port), debug=True)