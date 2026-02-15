from enum import Enum

class Status(Enum):
  CREATED = "created"
  PENDING = "pending"
  COMPLETED = "completed"

class Priority(Enum):
  LOW = "low"
  MEDIUM = "medium"
  HIGH = "high"

class Filter(Enum):
  NAME = "name"
  STATUS = "status"
  PRIORITY = "priority"
