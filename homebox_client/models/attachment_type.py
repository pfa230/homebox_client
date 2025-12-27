from enum import Enum

class AttachmentType(str, Enum):
    ATTACHMENT = "attachment"
    MANUAL = "manual"
    PHOTO = "photo"
    RECEIPT = "receipt"
    THUMBNAIL = "thumbnail"
    WARRANTY = "warranty"

    def __str__(self) -> str:
        return str(self.value)
