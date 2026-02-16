from flask.json import jsonify
from src.db.queries.manage_tasks import delete_task
from src.types.enums import Filter

def delete_a_task(filter: Filter, filter_value: str):
  try:
    delete_task(filter.value, filter_value)
    return jsonify({ "status": "success", "message": "task deleted!" })
  except Exception as err:
    return jsonify({ "status": "err", "message": f"{err}" })
