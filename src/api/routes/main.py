from flask import Blueprint, Response, request, jsonify
from src.api.controllers.create_task import create_new_task
from src.api.controllers.fetch_tasks import fetch_tasks
from src.api.controllers.delete_task import delete_a_task
from src.api.controllers.update_task import update_a_task
from src.types.enums import Priority, Status, Filter

routes = Blueprint('routes', __name__)

@routes.route("/", methods=["GET"])
def home():
  return "<h1>Hello World!</h1>"

@routes.route("/create-task", methods=["POST"])
def create_task() -> Response:
  if request.is_json:
    data = request.get_json()
    return create_new_task(data["name"], data["description"], Priority(data["priority"]))
  else:
    return jsonify({ "status": "err!", "message": "The request data type need to be a json!" })

@routes.route("/find-tasks", methods=["GET"])
def find_tasks() -> Response:
  filter = request.args.get("filter")
  filter_content = request.args.get("filter_content")

  if not filter:
    return fetch_tasks(None, None)
  if not filter_content:
    return jsonify({ "status": "err!", "message": "the filter_content is missing!!" })

  return fetch_tasks(Filter(filter), filter_content)

@routes.route("/delete-task", methods={"DELETE"})
def delete_task() -> Response:
  filter = request.args.get("filter")
  if not filter:
    return jsonify({ "status": "err!", "message": "the filter is missing!!" })

  filter_content = request.args.get("filter_content")

  if not filter_content:
    return jsonify({ "status": "err!", "message": "the filter content is missing!!" })
  return delete_a_task(Filter(filter), filter_content)

@routes.route("/update-task", methods=["PATCH"])
def update_task() -> Response:
  filter = request.args.get("filter")
  if not filter:
    return jsonify({ "status": "err!", "message": "the filter is missing!!" })

  filter_content = request.args.get("filter_content")
  name = request.args.get("name")
  description = request.args.get("description")
  priority = request.args.get("pripority")
  status = request.args.get("status")

  if not filter_content:
    return jsonify({ "status": "err!", "message": "the filter content is missing!!" })

  return update_a_task(
    Filter(filter), filter_content, name, description,
    Priority(priority) if priority is not None else None,
    Status(status) if status is not None else None,
  )
