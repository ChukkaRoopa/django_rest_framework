from django.urls import path
from . import views

urlpatterns = [
    # get all students path
    path('students/', views.studentsView),

    # get a single student
    path('students/<int:pk>/', views.sudentDetailView),

    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
]