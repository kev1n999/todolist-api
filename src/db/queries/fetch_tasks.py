from src.config import TASKS_COLLECTION

def fetch_tasks_(filter: str | None, filter_value: str | None) -> list:
  tasks = []
  if filter is None:
    tasks = list(TASKS_COLLECTION.find())
    return tasks

  match filter.strip().lower():
    case "name":
      tasks = list(TASKS_COLLECTION.find({ "name": filter_value }))
    case "status":
      tasks = list(TASKS_COLLECTION.find({ "status": filter_value }))
    case "priority":
      tasks = list(TASKS_COLLECTION.find({ "priority": filter_value }))
  return tasks
