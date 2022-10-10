from student.models import Student
from teacher.models import Teacher


def get_all_students(request):
    return {'allstudents': Student.objects.all()}


def get_all_teachers(request):
    return {'allteachers': Teacher.objects.all()}
