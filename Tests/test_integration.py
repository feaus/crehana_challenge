import random
import uuid
from typing import List

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
        integration_id=random.randint(1, 100),
        title=f'Testing title {random.randint(1, 1000)}',
        body=f'Testing body {random.randint(1, 1000)}',
        user_id=random.randint(1, 1000),
    )
    db.add(new_post)
    db.commit()
    posts = [new_post]
    yield posts
    for post in posts:
        db.delete(post)
        db.commit()


def test_store_post(storing_post: List[Posts]):
    body = {
        'title': f'Test {random.randint(1, 1000)}',
        'body': f'This is a test {random.randint(1, 1000)}',
        'user_id': random.randint(1, 1000),
    }
    response = client.post('/integration/posts', json=body)
    assert response.status_code == 201
    db_query = db.query(Posts).filter_by(
        title=body['title'],
        user_id=body['user_id'],
    ).first()
    assert db_query is not None
    storing_post.append(db_query)


def test_put_post(storing_post: List[Posts]):
    body = {
        'title': 'Editing title test',
        'body': 'Editing body test',
    }
    response = client.put(
        f'/integration/posts/{storing_post[0].id}', json=body)
    assert response.status_code == 200
    db_query = db.query(Posts).filter_by(
        id=storing_post[0].id,
        title=body['title'],
        body=body['body'],
    ).first()
    assert db_query is not None


def test_patch_post(storing_post: List[Posts]):
    body = {
        'title': 'Editing title test',
    }
    response = client.patch(
        f'/integration/posts/{storing_post[0].id}', json=body)
    assert response.status_code == 200
    db_query = db.query(Posts).filter_by(
        id=storing_post[0].id,
        title=body['title'],
    ).first()
    assert db_query is not None


def test_delete_post(storing_post: List[Posts]):
    response = client.delete(f'/integration/posts/{storing_post[0].id}')
    assert response.status_code == 200
    db_query = db.query(Posts).filter(
        Posts.id == storing_post[0].id,
        Posts.deleted_at == None,
    ).first()
    assert db_query is None
