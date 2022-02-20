import datetime
import uuid

from src.database.connection import SessionLocal
from src.database.models.posts import Posts
from src.serializers.posts import PostsModel


db = SessionLocal()


def delete_post_from_database(post_to_delete: Posts) -> None:
    post_to_delete.deleted_at = datetime.datetime.now()
    db.commit()
    return


def get_post_by_id(post_id: uuid.UUID) -> Posts:
    return db.query(Posts).filter(
        Posts.id == post_id,
        Posts.deleted_at == None,
    ).first()


def get_posts():
    for post in db.query(Posts).filter(Posts.deleted_at == None).all():
        yield post


def store_post(request_post: PostsModel) -> Posts:
    existing_post = db.query(Posts).filter(
        Posts.integration_id == request_post.integration_id,
        Posts.deleted_at == None,
    ).first()

    # if existing_post is not None:  # TODO: raise exception
    #     raise Exception

    new_post = Posts(
        id=uuid.uuid4(),
        integration_id=request_post.integration_id,
        title=request_post.title,
        body=request_post.body,
        user_id=request_post.user_id,
    )

    db.add(new_post)
    db.commit()

    return new_post


def update_post(existing_post: Posts, request_post: PostsModel) -> Posts:
    existing_post.title = request_post.title
    existing_post.body = request_post.body
    db.commit()
    return existing_post
