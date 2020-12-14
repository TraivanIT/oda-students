from django.urls import path
from .import views
urlpatterns = [
    path('', views.index , name = 'index'),
    path('books/', views.books, name = 'books'),
    path('students/', views.students, name='students'),
    path('student_details', views.student_details, name= 'student_details')

]
