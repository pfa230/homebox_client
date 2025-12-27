from enum import Enum

class ItemfieldType(str, Enum):
    BOOLEAN = "boolean"
    NUMBER = "number"
    TEXT = "text"
    TIME = "time"

    def __str__(self) -> str:
        return str(self.value)
