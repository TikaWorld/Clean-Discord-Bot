from entities.user import User
from entities.post import Post
from interface import logger


def create_post(post_id: str, content: str, user: User, secret:bool):
    new_post = Post(post_id=post_id, owner=user, text=content, secret=secret)
    logger.logging(new_post)
    return new_post


def update_post():
    NotImplemented


def delete_post():
    NotImplemented
