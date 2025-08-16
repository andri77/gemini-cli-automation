import requests

JSONPLACEHOLDER_API_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    response = requests.get(f"{JSONPLACEHOLDER_API_URL}/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_post_by_id():
    response = requests.get(f"{JSONPLACEHOLDER_API_URL}/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_create_post():
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(f"{JSONPLACEHOLDER_API_URL}/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == "foo"
