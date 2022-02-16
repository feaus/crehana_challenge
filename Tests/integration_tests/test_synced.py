import random
import uuid

import pytest
from fastapi.testclient import TestClient

from src.database.connection import SessionLocal
from src.database.models.posts import Posts
from src.main import app


client = TestClient(app)
db = SessionLocal()


@pytest.fixture
def storing_post():
    new_post = Posts(
        id=uuid.uuid4(),
        integration_id=random.randint(1, 1000),
        title=f'Testing title {random.randint(1, 1000)}',
        body=f'Testing body {random.randint(1, 1000)}',
        user_id=random.randint(1, 1000),
    )
    db.add(new_post)
    db.commit()
    yield new_post
    db.delete(new_post)
    db.commit()


def test_get_posts(storing_post: Posts):
    response = client.get('/synced/posts')
    assert response.status_code == 200
    posts = db.query(Posts).all()
    assert storing_post in posts


def test_get_post(storing_post: Posts):
    response = client.get(f'/synced/posts/{storing_post.id}')
    assert response.status_code == 200
    post_query = db.query(Posts).filter(Posts.id == storing_post.id).first()
    assert post_query is not None
