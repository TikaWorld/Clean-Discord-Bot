from dataclasses import dataclass, field

from datetime import datetime


@dataclass(frozen=True)
class Post:
    post_id: str
    owner_id: str
    text: str
    secret: bool
    created_at: datetime = field(default_factory=datetime.now)
