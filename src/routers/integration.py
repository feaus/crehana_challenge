import os
import uuid

import requests

from fastapi import APIRouter, status

from src.controllers.posts import (
    delete_post_from_database, get_post_by_id, store_post, update_post)
from src.schemas.posts import PostsModel


router = APIRouter(
    prefix='/integration',
)


@router.post('/posts', status_code=status.HTTP_201_CREATED)
def save_post(post: PostsModel):
    base_url = os.environ.get('THIRD_PARTY_URL')

    request_body = {
        'title': post.title,
        'body': post.body,
        'user_id': post.user_id,
    }
    response = requests.post(f'{base_url}/posts', json=request_body)

    # if response.status_code != 201:  # TODO: exception
    #     raise Exception

    new_id = response.json()['id']

    post.integration_id = new_id

    new_post = store_post(request_post=post)

    return {
        'message': 'Post stored successfully',
        'data': [{'id': new_post.id}],
    }


@router.put('/posts/{post_id}', status_code=status.HTTP_200_OK)
def put_post(post_id: uuid.UUID, post: PostsModel):
    stored_post = get_post_by_id(post_id)

    # if stored_post is None:  # TODO: exception
    #     raise Exception

    base_url = os.environ.get('THIRD_PARTY_URL')

    request_body = {
        'title': post.title,
        'body': post.body,
        'user_id': post.user_id,
    }
    response = requests.put(f'{base_url}/posts/{post_id}', json=request_body)

    # if response.status_code != 200:  # TODO: exception
    #     raise Exception

    updated_post = update_post(existing_post=stored_post, request_post=post)

    return {
        'message': 'Post updated successfully',
        'data': [{'id': updated_post.id}]
    }


@router.patch('/posts/{post_id}', status_code=status.HTTP_200_OK)
def patch_post(post_id: uuid.UUID, post: PostsModel):
    stored_post = get_post_by_id(post_id)

    # if stored_post is None:  # TODO: exception
    #     raise Exception

    base_url = os.environ.get('THIRD_PARTY_URL')

    request_body = {
        'title': post.title,
        'body': post.body,
        'user_id': post.user_id,
    }
    response = requests.patch(f'{base_url}/posts/{post_id}', json=request_body)

    # if response.status_code != 200:  # TODO: exception
    #     raise Exception

    updated_post = update_post(existing_post=stored_post, request_post=post)

    return {
        'message': 'Post updated successfully',
        'data': [{
            'id': updated_post.id,
            'user_id': updated_post.user_id,
            'body': updated_post.body,
            'title': updated_post.title,
            'integration_id': updated_post.integration_id,
        }]
    }


@router.delete('/posts/{post_id}', status_code=status.HTTP_200_OK)
def delete_post(post_id: uuid.UUID):
    stored_post = get_post_by_id(post_id)

    # if stored_post is None:  # TODO: exception
    #     raise Exception

    base_url = os.environ.get('THIRD_PARTY_URL')
    response = requests.delete(f'{base_url}/posts/{post_id}')

    # if response.status_code != 200:  # TODO: exception
    #     raise Exception

    delete_post_from_database(stored_post)

    return {
        'message': 'Post deleted successfully',
        'data': []
    }
