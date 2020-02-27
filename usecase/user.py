from entities.user import User


def get_user(user_id, user_name):
    return User(user_id, user_name)
