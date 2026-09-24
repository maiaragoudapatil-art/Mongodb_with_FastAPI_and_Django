from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["fastapi_student_db"]

student_collection = db["students"]