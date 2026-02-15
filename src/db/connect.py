from pymongo import MongoClient

def mongo_connect(mongo_uri: str | None) -> MongoClient | None:
  try:
    if mongo_uri is None:
      raise Exception("Mongo URI is missing!!")
    mongo_client = MongoClient(mongo_uri)
    print("Connect with MongoDB!")
    return mongo_client
  except Exception as err:
    print(f"an error ocurred to connect with pymongo!\n{err}")
