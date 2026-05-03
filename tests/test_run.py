import requests

class MockResponse:
    status_code = 200

def test_requests_status(monkeypatch):
    def mock_get(url):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    r = requests.get("https://api.github.com")
    assert r.status_code == 200
