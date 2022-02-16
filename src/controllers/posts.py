import uuid

from src.database.connection import SessionLocal
from src.database.models.posts import Posts
from src.schemas.posts import PostsModel


db = SessionLocal()


def delete_post_from_database(post_to_delete: Posts) -> None:
    db.delete(post_to_delete)
    db.commit()
    return


def get_post_by_id(post_id: uuid.UUID) -> Posts:
    return db.query(Posts).filter(Posts.id == post_id).first()


def get_posts():
    yield db.query(Posts).all()  # TODO: yield or return?


def store_post(request_post: PostsModel) -> Posts:
    existing_post = db.query(Posts).filter(
        Posts.integration_id == request_post.integration_id
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
