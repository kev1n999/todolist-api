if __name__ == "__main__":
  from .config import MONGO_URI
  from .db.connect import mongo_connect
  from .api.main import api

  if MONGO_URI is None:
    raise Exception("Mongo URI is missing!!")

  mongo_connect(MONGO_URI)

  app = api()
  app.run(host="127.0.0.1", port=8000)
