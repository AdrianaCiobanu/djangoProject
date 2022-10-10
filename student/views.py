# from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from student.filters import StudentFilter
from student.forms import StudentForm, StudentUpdateForm
from student.models import Student


# from teacher.models import Teacher


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'student/create_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('list_of_students')
    permission_required = 'student.add_student'


class StudentsListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'all_students'
    permission_required = 'student.list_of_students'

    def get_context_data(self, **kwargs):
        context = super(StudentsListView, self).get_context_data(**kwargs)
        # all_teachers = Teacher.objects.all()
        # context['teachers'] = all_teachers
        all_students = Student.objects.all()
        student_filter = StudentFilter(self.request.GET, queryset=all_students)
        all_students = student_filter.qs
        context['all_students'] = all_students
        context['student_filter'] = student_filter

        return context


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('list_of_students')
    permission_required = 'student.change_student'


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'student/details_student.html'
    model = Student
    permission_required = 'student.view_student'


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list_of_students')
    permission_required = 'student.delete_student'


@login_required()
@permission_required('student.delete_student')
def delete_student(request, pk):
    Student.objects.filter(id=pk).delete()
    return redirect('list_of_students')
