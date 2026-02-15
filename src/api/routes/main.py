from flask import Blueprint, Response, request, jsonify
from src.api.controllers.create_task import create_new_task
from src.types.enums import Priority, Status

routes = Blueprint('routes', __name__)

@routes.route("/", methods=["GET"])
def home():
  return "<h1>Hello World!</h1>"

@routes.route("/create-task", methods=["POST"])
def create_task() -> Response:
  if request.is_json:
    data = request.get_json()
    return create_new_task(data["name"], data["description"], Status(data["status"]), Priority(data["priority"]))
  else:
    return jsonify({ "status": "err!", "message": "The request data type need to be a json!" })
