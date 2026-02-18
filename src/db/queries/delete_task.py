from src.config import TASKS_COLLECTION
from src.errors import TaskNotExists

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
    raise TaskNotExists("the task doesn't exists!")
  try:
    TASKS_COLLECTION.delete_one({ fil: filter_value })
  except Exception as err:
    print(f"an error ocurred to delete tasks: {err}")
