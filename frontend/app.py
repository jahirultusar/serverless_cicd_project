from flask import Flask, jsonify, render_template, request
import random
import os
import urllib.request
import urllib.parse
import json

app = Flask(__name__)

quotes = [
    {"quote": "The best way to get started is to quit talking and begin doing.", "author": "Walt Disney"},
    {"quote": "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty.", "author": "Winston Churchill"},
    {"quote": "Don't let yesterday take up too much of today.", "author": "Will Rogers"},
    {"quote": "You learn more from failure than from success. Don't let it stop you.", "author": "Unknown"},
    {"quote": "It's not whether you get knocked down, it's whether you get up.", "author": "Vince Lombardi"},
    {"quote": "If you are working on something that you really care about, you don't have to be pushed. The vision pulls you.", "author": "Steve Jobs"},
    {"quote": "People who are crazy enough to think they can change the world, are the ones who do.", "author": "Rob Siltanen"},
    {"quote": "Failure will never overtake me if my determination to succeed is strong enough.", "author": "Og Mandino"},
    {"quote": "We may encounter many defeats but we must not be defeated.", "author": "Maya Angelou"},
    {"quote": "Knowing is not enough; we must apply. Wishing is not enough; we must do.", "author": "Johann Wolfgang Von Goethe"},
    {"quote": "Imagine your life is perfect in every respect; what would it look like?", "author": "Brian Tracy"},
    {"quote": "We generate fears while we sit. We overcome them by action.", "author": "Dr. Henry Link"},
    {"quote": "Whether you think you can or think you can't, you're right.", "author": "Henry Ford"},
    {"quote": "Security is mostly a superstition. Life is either a daring adventure or nothing.", "author": "Helen Keller"},
    {"quote": "The man who has confidence in himself gains the confidence of others.", "author": "Hasidic Proverb"},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quote')  
def get_quote():
    return jsonify(random.choice(quotes))

@app.route('/lambda')
def lambda_page():
    return render_template('lambda.html')

@app.route('/invoke-lambda', methods=['POST'])
def invoke_lambda():
    weather_url = os.environ.get('LAMBDA_WEATHER_URL', '')
    time_url    = os.environ.get('LAMBDA_TIME_URL', '')

    data  = request.get_json() or {}
    skill = data.get('skill', 'weather')

    if skill == 'time':
        if not time_url:
            return jsonify({"error": "LAMBDA_TIME_URL not set — complete the bonus exercise to enable this skill"}), 500
        url = time_url
    else:
        if not weather_url:
            return jsonify({"error": "LAMBDA_WEATHER_URL environment variable not set"}), 500
        city = data.get('city', 'london')
        url  = f"{weather_url}?city={urllib.parse.quote(city)}"

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            body = json.loads(resp.read().decode('utf-8'))
        return jsonify({"response": body.get("message", body)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)