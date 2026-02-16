from src.config import TASKS_COLLECTION
from src.errors import TaskAlreadyExists, TaskNotExists

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

def delete_task(filter: str, filter_value: str):
  task = None
  fil = filter.strip().lower()
  match fil:
    case "name":
      task = TASKS_COLLECTION.find_one({ "name": filter_value })
    case "status":
      task = TASKS_COLLECTION.find_one({ "status": filter_value })
    case "priority":
      task = TASKS_COLLECTION.find_one({ "priority": filter_value })

  if task is None:
    TaskNotExists("the task doesn't exists!")
  try:
    TASKS_COLLECTION.delete_one({ fil: filter_value })
  except Exception as err:
    print(f"an error ocurred to delete tasks: {err}")
