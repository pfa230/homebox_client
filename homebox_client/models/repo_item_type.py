from enum import Enum

class RepoItemType(str, Enum):
    ITEM = "item"
    LOCATION = "location"

    def __str__(self) -> str:
        return str(self.value)
