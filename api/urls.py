from django.urls import path
from . import views

urlpatterns = [
    # get all students path
    path('students/', views.studentsView),

    # get a single student
    path('students/<int:pk>/', views.sudentDetailView),
]