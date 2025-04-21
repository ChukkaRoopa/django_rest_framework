from django.shortcuts import render, HttpResponse

# Create your views here.
def students(request):
    students = [
        {'id': 1, 'name': "John", 'age': 24}
    ]
    return HttpResponse(students)