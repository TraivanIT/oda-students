from django.shortcuts import render
from .models import Classes, Book, Student

# Create your views here.

def index(request):
    student_total = Student.objects.count()
    active_student_total = Student.objects.all().filter(graduted=False).count()
    graduted_student_total = Student.objects.all().filter(graduted=True).count()
    computer_student_total = Student.objects.all().filter(studyComputer=True).count()


    context = {
        'studentTotal': student_total,
        'activeStudentTotal': active_student_total,
        'gradutedStudentTotal': graduted_student_total,
        'computerStudentTotal': computer_student_total,
        }
    return render(request, 'main/index.html', context)


def student_details(request):
    students = Student.objects.all().count()
    context = {'students': students}
    return render(request, 'main/student_details.html',context)


def books(request):
    all_classes = Classes.objects.all()
    all_books = Book.objects.all()
    context = {'allClasses': all_classes, 'allBooks': all_books}
    return render(request, 'main/books.html', context)


def students(request):
    return render(request, 'main/students.html')
