from flask import jsonify, Response
from src.db.queries.create_task import create_task
from src.types.enums import Priority
from typing import Union

def create_new_task(name: str, description: str, priority: Priority) -> Union[Response, tuple[Response, int]]:
  try:
    create_task(name, description, priority=priority.value)
    return jsonify({ "status": "success!", "message": "task created!" }), 200
  except Exception as err:
    return jsonify({ "err": "an error ocurred to create task!", "message": f"{err}" }), 400
