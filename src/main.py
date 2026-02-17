if __name__ == "__main__":
  from .api.main import api
  from .config import DB, SERVER_PORT

  app = api()
  app.run(host="127.0.0.1", port=SERVER_PORT)
