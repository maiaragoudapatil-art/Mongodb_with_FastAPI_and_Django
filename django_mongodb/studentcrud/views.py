from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .mongodb import student_collection
import json


def home(request):
    return JsonResponse({
        "message": "Django MongoDB Working"
    })


@csrf_exempt
def students(request):

    # CREATE
    if request.method == "POST":

        data = json.loads(request.body)

        existing_student = student_collection.find_one(
            {"student_id": data["student_id"]}
        )

        if existing_student:
            return JsonResponse({
                "message": "Student ID already exists"
            })

        student_collection.insert_one(data)

        return JsonResponse({
            "message": "Student Created"
        })

    # READ ALL
    elif request.method == "GET":

        students = []

        for student in student_collection.find():

            student["_id"] = str(student["_id"])

            students.append(student)

        return JsonResponse(
            students,
            safe=False
        )

    return JsonResponse({
        "message": "Method Not Allowed"
    })


@csrf_exempt
def student_detail(request, student_id):

    # READ ONE
    if request.method == "GET":

        student = student_collection.find_one(
            {"student_id": student_id}
        )

        if student:

            student["_id"] = str(student["_id"])

            return JsonResponse(student)

        return JsonResponse({
            "message": "Student Not Found"
        })

    # UPDATE
    elif request.method == "PUT":

        data = json.loads(request.body)

        result = student_collection.update_one(
            {"student_id": student_id},
            {"$set": data}
        )

        if result.matched_count == 0:
            return JsonResponse({
                "message": "Student Not Found"
            })

        return JsonResponse({
            "message": "Student Updated"
        })

    # DELETE
    elif request.method == "DELETE":

        result = student_collection.delete_one(
            {"student_id": student_id}
        )

        if result.deleted_count == 0:
            return JsonResponse({
                "message": "Student Not Found"
            })

        return JsonResponse({
            "message": "Student Deleted"
        })

    return JsonResponse({
        "message": "Method Not Allowed"
    })