from django.views.generic import ListView
from django.shortcuts import render

from .models import Student,Teacher,Students_teachers


def students_list(request):
    students = Student.objects.all()
    ordering = students.order_by('group')
    teachers = Teacher.objects.all()
    students_teachers = Students_teachers.objects.all()
    template = 'school/students_list.html'
    context = {'object_list': ordering}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    return render(request, template, context)
