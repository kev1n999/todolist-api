from flask import Blueprint

routes = Blueprint('routes', __name__)

@routes.get("/")
def home():
  return "<h1>Hello World!</h1>"
