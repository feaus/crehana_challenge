import uuid

from fastapi import APIRouter

from src.controllers.posts import get_post_by_id, get_posts
from src.exceptions import ResourceNotFound


router = APIRouter(
    prefix='/synced',
)


@router.get('/posts')
def get_synced_posts():
    stored_posts = get_posts()
    return {
        'message': 'Synced posts returned successfully',
        'data': stored_posts,
    }


@router.get('/posts/{post_id}')
def get_synced_post(post_id: uuid.UUID):
    stored_post = get_post_by_id(post_id)

    if stored_post is None:
        raise ResourceNotFound(resource='post', id_=post_id)

    return {
        'message': 'Synced post returned successfully',
        'data': [stored_post],
    }
