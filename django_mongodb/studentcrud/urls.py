from django.urls import path

from .views import (
    home,
    students,
    student_detail
)

urlpatterns = [

    path('', home),

    path('students/', students),

    path('students/<int:student_id>/', student_detail),
]