from pymongo import MongoClient, database

def mongo_connect(mongo_uri: str | None) -> database.Database | None:
  try:
    if mongo_uri is None:
      raise Exception("Mongo URI is missing!!")

    mongo_client = MongoClient(mongo_uri)
    database = mongo_client.get_database("todolist")
    print("Connect with MongoDB!")
    return database
  except Exception as err:
    print(f"an error ocurred to connect with pymongo!\n{err}")
