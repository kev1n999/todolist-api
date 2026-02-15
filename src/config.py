import os
from dotenv import load_dotenv
from .db.connect import mongo_connect

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB = mongo_connect(MONGO_URI)
TASKS_COLLECTION = DB.get_collection("tasks")
