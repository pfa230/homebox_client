from enum import Enum

class GetV1MaintenanceStatus(str, Enum):
    BOTH = "both"
    COMPLETED = "completed"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
