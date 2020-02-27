from dataclasses import dataclass, field

from datetime import datetime

from entities.user import User


@dataclass(frozen=True)
class Post:
    post_id: str
    owner: User
    text: str
    secret: bool
    created_at: datetime = field(default_factory=datetime.now)
