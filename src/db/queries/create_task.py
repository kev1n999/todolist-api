from src.config import TASKS_COLLECTION
from src.errors import TaskAlreadyExists
from src.types.enums import Status

def create_task(name: str, description: str, *, priority: str):
  task_exists = TASKS_COLLECTION.find_one({ "name": name })
  if task_exists:
    raise TaskAlreadyExists("the task already exists!")
  try:
    TASKS_COLLECTION.insert_one({
      "name": name,
      "description": description,
      "status": Status.CREATED.value,
      "priority": priority,
    })
  except Exception as err:
    print(f"an error ocurred to create task!\n{err}")
