from flask import Flask
from .routes.main import routes

def api() -> Flask:
  app = Flask(__name__)
  app.register_blueprint(routes)

  return app
