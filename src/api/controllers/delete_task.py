from flask import Response
from flask.json import jsonify
from src.db.queries.delete_task import delete_task
from src.types.enums import Filter
from typing import Union

def delete_a_task(filter: Filter, filter_value: str) ->Union[Response, tuple[Response, int]]:
  try:
    delete_task(filter.value, filter_value)
    return jsonify({ "status": "success", "message": "task deleted!" }), 200
  except Exception as err:
    return jsonify({ "status": "err", "message": f"{err}" }), 400
