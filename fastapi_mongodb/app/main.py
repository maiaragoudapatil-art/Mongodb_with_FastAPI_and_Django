from fastapi import FastAPI
from app.database import student_collection
from app.models import Student
from bson import ObjectId

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "FastAPI Working Successfully",
        "database": "fastapi_student_db"
    }

@app.post("/students")
def create_student(student: Student):

    result = student_collection.insert_one(
        student.model_dump()
    )

    return {
        "message": "Student Created",
        "id": str(result.inserted_id)
    }

@app.get("/students")
def get_students():

    students = []

    for student in student_collection.find():

        student["_id"] = str(student["_id"])

        students.append(student)

    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):

    student = student_collection.find_one(
        {"student_id": student_id}
    )

    if student:
        student["_id"] = str(student["_id"])

    return student

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):

    student_collection.update_one(
        {"student_id": student_id},
        {"$set": student.model_dump()}
    )

    return {
        "message": "Student Updated"
    }
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    student_collection.delete_one(
        {"student_id": student_id}
    )

    return {
        "message": "Student Deleted"
    }

@app.post("/students")
def create_student(student: Student):

    existing_student = student_collection.find_one(
        {"student_id": student.student_id}
    )

    if existing_student:
        return {
            "message": "Student ID already exists"
        }

    result = student_collection.insert_one(
        student.model_dump()
    )

    return {
        "message": "Student Created",
        "id": str(result.inserted_id)
    }
    
@app.post("/students")
def create_student(student: Student):

    existing_student = student_collection.find_one(
        {"student_id": student.student_id}
    )

    if existing_student:
        return {
            "message": "Student ID already exists"
        }

    result = student_collection.insert_one(
        student.model_dump()
    )

    return {
        "message": "Student Created",
        "id": str(result.inserted_id)
    }