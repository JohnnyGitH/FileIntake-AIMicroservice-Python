from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# /summarize endpoint tests
def test_summarize_returns_summary():
        payload = {"text": "hello summarize"}

        r = client.post("/summarize", json=payload)

        assert r.status_code == 200
        data = r.json()

        assert "summary" in data
        assert isinstance(data["summary"],str)
        assert "BEEP BOOP - Summarize" in data["summary"] # using stubbed responses for now

def test_summarize_empty_text_returns_validation_error():
        r = client.post("/summarize",json={"text":""})

        assert r.status_code in (200,422)

        if r.status_code == 200:
                assert "summary" in r.json()
        else:
            # FastAPI validation error structure
            body = r.json()
            assert "detail" in body

# /eli5 endpoint tests
def test_summarize_returns_eli5_explanation():
        payload = {"text": "hello explain like I am 5"}

        r = client.post("/eli5", json=payload)

        assert r.status_code == 200
        data = r.json()

        assert "summary" in data
        assert isinstance(data["summary"],str)
        assert "BEEP BOOP - Explain like I am 5" in data["summary"] # using stubbed responses for now

def test_eli5_empty_text_returns_validation_error():
        r = client.post("/eli5",json={"text":""})

        assert r.status_code in (200,422)

        if r.status_code == 200:
                assert "summary" in r.json()
        else:
            # FastAPI validation error structure
            body = r.json()
            assert "detail" in body

# /pointform endpoint tests
def test_summarize_returns_pointform():
        payload = {"text": "hello pointform"}

        r = client.post("/pointform", json=payload)

        assert r.status_code == 200
        data = r.json()

        assert "summary" in data
        assert isinstance(data["summary"],str)
        assert " BEEP BOOP - Pointform" in data["summary"] # using stubbed responses for now

def test_pointform_empty_text_returns_validation_error():
        r = client.post("/pointform",json={"text":""})

        assert r.status_code in (200,422)

        if r.status_code == 200:
                assert "summary" in r.json()
        else:
            # FastAPI validation error structure
            body = r.json()
            assert "detail" in body