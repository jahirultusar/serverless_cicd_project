import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lambda_function import lambda_handler



def test_lambda_returns_weather_for_known_city():
    event = {"queryStringParameters": {"city": "london"}}

    response = lambda_handler(event, None)

    assert response["statusCode"] == 200
    body = json.loads(response["body"])
    assert "message" in body
    assert "London" in body["message"]


def test_lambda_returns_400_for_unknown_city():
    event = {"queryStringParameters": {"city": "madrid"}}

    response = lambda_handler(event, None)

    assert response["statusCode"] == 400
    body = json.loads(response["body"])
    assert "Sorry" in body["message"]