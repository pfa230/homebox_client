from enum import Enum

class RepoMaintenanceFilterStatus(str, Enum):
    BOTH = "both"
    COMPLETED = "completed"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
