from src.config import TASKS_COLLECTION
from src.errors import TaskAlreadyExists

def create_task(name: str, description: str, status: str, priority: str):
  task_exists = TASKS_COLLECTION.find_one({ "name": name })
  if task_exists:
    raise TaskAlreadyExists("the task already exists!")
  try:
    TASKS_COLLECTION.insert_one({
      "name": name,
      "description": description,
      "status": status,
      "priority": priority,
    })
  except Exception as err:
    print(f"an error ocurred to create task!\n{err}")

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
