from flask import jsonify, Response
from src.db.queries.fetch_tasks import fetch_tasks_
from src.types.enums import Filter
from src.api.utils.serialize_task import serialize_task

def fetch_tasks(filter: Filter | None, filter_content: str | None) -> Response:
  try:
    tasks = fetch_tasks_(filter.value if filter is not None else None, filter_content)
    serialized = [serialize_task(task) for task in tasks]
    return jsonify(serialized)
  except Exception as err:
    return jsonify({ "err": "an error ocurred to create task!", "message": f"{err}" })
