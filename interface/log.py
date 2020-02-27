from entities.post import Post


class LoggerInterface:
    def logging(self, post: Post):
        NotImplemented


def post2log(post):
    return f"{post.owner.name}({post.secret}): {post.text}"


class LocalLogger(LoggerInterface):
    def __init__(self):
        self.log = []

    def logging(self, post):
        self.log.append(post2log(post))

    def get_log(self):
        return self.log
