import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home_page_returns_200(client):
    """Home page should return a 200 status code."""
    response = client.get('/')
    assert response.status_code == 200

def test_quote_route_returns_200(client):
    """Quote route should return a 200 status code."""
    response = client.get('/quote')
    assert response.status_code == 200

def test_quote_returns_json(client):
    """Quote route should return JSON."""
    response = client.get('/quote')
    assert response.content_type == 'application/json'

def test_quote_has_required_fields(client):
    """Quote response should contain quote and author fields."""
    response = client.get('/quote')
    data = response.get_json()
    assert 'quote' in data
    assert 'author' in data

def test_lambda_page_returns_200(client):
    """Lambda demo page should return a 200 status code."""
    response = client.get('/lambda')
    assert response.status_code == 200