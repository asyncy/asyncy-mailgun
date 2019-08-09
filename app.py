import os
import json
import requests
from flask import Flask, make_response, request

app = Flask(__name__)

API_KEY = os.environ['API_KEY']
DOMAIN = os.environ['DOMAIN']

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    print(data)
    if data.get("to") is None or data.get("to") == "" :
        return end({
            'success': False,
            'error': "'to' parameter is missing"
        }),400
    elif data.get("text") is None or data.get("text") == "" :
        return end({
            'success': False,
            'error': "'text' parameter is missing"
        }),400
    elif data.get("from") is None or data.get("from") == "" :
        return end({
            'success': False,
            'error': "'from' parameter is missing"
        }),400
    res = requests.post(
        "https://api.mailgun.net/v3/"+DOMAIN+"/messages",
        auth=("api", API_KEY),
        data=data
    )

    if res.status_code != 200:
        return end({
            'success': False,
            'error': f'Mailgun responded with a {res.status_code}!'
        }),res.status_code
    return end(res.json()), res.status_code

def end(res):
    resp = make_response(json.dumps(res))
    resp.headers['Content-Type'] = 'application/json; charset=utf-8'
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
