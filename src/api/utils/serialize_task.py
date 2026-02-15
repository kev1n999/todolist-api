def serialize_task(task: dict) -> dict:
  task = dict(task)
  if "_id" in task:
    task["_id"] = str(task["_id"])
  return task
