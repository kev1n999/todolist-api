from flask import jsonify, Response
from src.db.queries.update_task import update_task
from src.types.enums import Priority, Status, Filter

def update_a_task(
  filter: Filter,
  filter_content: str,
  name: str | None,
  description: str | None,
  priority: Priority | None,
  status: Status | None,
):
  try:
    priority_value = ""
    status_value = ""
    if priority is not None:
      priority_value += priority.value
    if status is not None:
      status_value += status.value

    update_task(filter.value, filter_content, name, description, priority_value, status_value)
    return jsonify({ "status": "success", "message": "task updated!" })
  except Exception as err:
    return jsonify({ "err": "an error ocurred to update task!", "message": f"{err}" })
