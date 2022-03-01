"""Api tests."""

from fastapi.testclient import TestClient

from app.api.main import app

# Test client that will make requests to our app process.
client = TestClient(app)


# Dummy test to check if server and test-client work and can talk to each other.
def test_ping() -> None:
    """First test so make sure the server is running."""
    res = client.get("/ping")
    assert res.status_code == 200
    assert res.json() == {"msg": "pong"}
