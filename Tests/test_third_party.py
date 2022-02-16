import random

from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_get_posts():
    response = client.get('/thirdParty/posts')
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body['data'], list)


def test_get_post():
    post_id = random.randint(1, 100)
    response = client.get(f'/thirdParty/posts/{post_id}')
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body['data'], list)


def test_get_post_comments():
    post_id = random.randint(1, 100)
    response = client.get(f'/thirdParty/posts/{post_id}/comments')
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body['data'], list)


def test_get_comments():
    response = client.get('/thirdParty/comments')
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body['data'], list)


def test_get_comments_query():
    post_id = random.randint(1, 100)
    response = client.get(f'/thirdParty/comments?post_id={post_id}')
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body['data'], list)
