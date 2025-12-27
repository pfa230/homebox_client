from enum import Enum

class AuthrolesRole(str, Enum):
    ADMIN = "admin"
    ATTACHMENTS = "attachments"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
