from src.config import TASKS_COLLECTION
from src.errors import TaskNotExists

def update_task(
  filter: str,
  filter_content: str,
  name: str | None,
  description: str | None,
  priority: str | None,
  status: str | None,
):
  task_exists = TASKS_COLLECTION.find_one({ filter: filter_content })
  if not task_exists:
    raise TaskNotExists("the task already exists!")

  try:
    TASKS_COLLECTION.update_one({ filter: filter_content }, update={ "$set": {
      "name": name,
      "description": description,
      "priority": priority,
      "status": status,
    } })
  except Exception as err:
    raise Exception(err)
