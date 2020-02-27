from dataclasses import dataclass


@dataclass(frozen=True)
class Channel:
    channel_id: str
