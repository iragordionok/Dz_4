from django.contrib import admin

from .models import Student, Teacher, Students_teachers


class Students_teachersInline(admin.TabularInline):
    model = Students_teachers
    extra = 3

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [Students_teachersInline,]
