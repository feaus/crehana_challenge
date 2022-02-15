import os
import requests
from typing import Optional

from fastapi import APIRouter

# from engine.exception_models import ExternalError  # TODO: custom exceptions


router = APIRouter(
    prefix='/thirdParty',
)


@router.get('/posts')
def get_third_party_posts():
    base_url = os.environ.get('THIRD_PARTY_URL')
    response = requests.get(f'{base_url}/posts')
    # raise ExternalError  # TODO: raise exception if third-party fails
    return {
        'message': "Third party's posts returned successfully",
        'data': response.json(),
    }


@router.get('/posts/{post_id}')
def get_post_by_id(post_id: int):
    base_url = os.environ.get('THIRD_PARTY_URL')
    response = requests.get(f'{base_url}/posts/{post_id}')
    # raise ExternalError  # TODO: raise exception if third-party fails
    return {
        'message': "Third party's post returned successfully",
        'data': [response.json()],
    }


@router.get('/posts/{post_id}/comments')
def get_post_comment(post_id: int):
    base_url = os.environ.get('THIRD_PARTY_URL')
    response = requests.get(f'{base_url}/posts/{post_id}/comments')
    # raise ExternalError  # TODO: raise exception if third-party fails
    return {
        'message': "Third party's post's comments returned successfully",
        'data': response.json(),
    }


@router.get('/comments')
def get_comments(post_id: Optional[int] = None):
    base_url = os.environ.get('THIRD_PARTY_URL')
    url = f'{base_url}/comments'
    if post_id:
        url += f'?postId={post_id}'
    response = requests.get(url)
    # raise ExternalError  # TODO: raise exception if third-party fails
    return {
        'message': "Third party's post's comments returned successfully",
        'data': response.json(),
    }
