from django.shortcuts import render, redirect
from .models import Student

from django.contrib import messages
from django.db import IntegrityError

def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        course = request.POST['course']

        try:
            Student.objects.create(
                name=name,
                email=email,
                course=course
            )
            messages.success(request, "Student added successfully!")
            return redirect('student_list')

        except IntegrityError:
            messages.error(request, "Email already exists!")

    return render(request, 'students/add_student.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')

def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.save()
        return redirect('student_list')

    return render(request, 'students/edit_student.html', {'student': student})

