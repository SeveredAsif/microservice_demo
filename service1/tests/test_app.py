# service1/tests/test_app.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pytest
from app import app

# Use Flask's test client
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the '/' endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == "Hello from Service 1!"

def test_call_service2(client, monkeypatch):
    """Test '/call-service2' endpoint with mocked requests"""
    import requests

    class MockResponse:
        def json(self):
            return {'message': 'Hello from Service 2!'}
    def mock_get(url):
        return MockResponse()

    # Patch requests.get to avoid real HTTP call
    monkeypatch.setattr(requests, "get", mock_get)

    response = client.get('/call-service2')
    assert response.status_code == 200
    data = response.get_json()
    assert "Service 1 received: Hello from Service 2!" in data['message']
