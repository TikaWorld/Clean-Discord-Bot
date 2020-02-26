from dataclasses import dataclass


@dataclass(frozen=True)
class Admin:
    admin_id: str
    name: str
