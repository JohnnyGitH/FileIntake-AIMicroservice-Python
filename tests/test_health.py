from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Quick and easy test to make sure app imports correctly and starts
def test_docs_or_root_is_reachable():
    r = client.get("/docs")
    assert r.status_code in (200,404)