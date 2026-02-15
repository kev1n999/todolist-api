if __name__ == "__main__":
  from .config import MONGO_URI
  from .db.connect import mongo_connect

  if MONGO_URI is None:
    raise Exception("Mongo URI is missing!!")

  mongo_connect(MONGO_URI)
