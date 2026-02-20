from flask import Flask
from flask_cors import CORS
from .routes.main import routes

def api() -> Flask:
  app = Flask(__name__)
  CORS(app)
  app.register_blueprint(routes)

  return app
