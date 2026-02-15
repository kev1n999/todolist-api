from flask import jsonify, Response
from src.db.queries.manage_tasks import create_task
from src.types.enums import Priority, Status

def create_new_task(name: str, description: str, status: Status, priority: Priority) -> Response:
  try:
    create_task(name, description, status.value, priority.value)
    return jsonify({ "status": "success!", "message": "task created!" })
  except Exception as err:
    return jsonify({ "err": "an error ocurred to create task!", "message": f"{err}" })
