from enum import Enum

class Status(Enum):
  CREATED = "created"
  PENDING = "pending"
  COMPLETED = "completed"

class Priority(Enum):
  LOW = "low"
  MEDIUM = "medium"
  HIGH = "high"
