from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee')

urlpatterns = [
    # get all students path
    path('students/', views.studentsView),

    # get a single student
    path('students/<int:pk>/', views.sudentDetailView),

    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view()),

    # using viewset
    path('', include(router.urls)),

    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view()),

    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]