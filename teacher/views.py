from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from rest_framework.response import Response
from rest_framework.views import APIView

from student.models import Student
from teacher.filters import TeacherFilter
from teacher.forms import TeacherForm, TeacherUpdateForm
from teacher.models import Teacher
from teacher.serializers import TeacherSerializer


class TeacherCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'teacher/create_teacher.html'
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy('homepage')
    permission_required = 'teacher.add_teacher'


class TeachersListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'teacher/list_of_teachers.html'
    model = Teacher
    context_object_name = 'all_teachers'
    permission_required = 'teacher.list_of_teachers'

    def get_context_data(self, **kwargs):
        context = super(TeachersListView, self).get_context_data(**kwargs)
        all_teachers = Teacher.objects.all()
        teacher_filter = TeacherFilter(self.request.GET, queryset=all_teachers)
        all_teachers = teacher_filter.qs
        context['all_teachers'] = all_teachers
        context['teacher_filter'] = teacher_filter

        return context


class TeacherUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'teacher/update_teacher.html'
    model = Teacher
    form_class = TeacherUpdateForm
    success_url = reverse_lazy('list_of_teachers')
    permission_required = 'teacher.change_teacher'


class TeacherDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'teacher/details_teacher.html'
    model = Teacher
    permission_required = 'teacher.view_teacher'


class TeacherDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'teacher/delete_teacher.html'
    model = Teacher
    success_url = reverse_lazy('list_of_teachers')
    permission_required = 'teacher.delete_teacher'


@login_required()
@permission_required('teacher.delete_teacher')
def delete_teacher(request, pk):
    Teacher.objects.filter(id=pk).delete()
    return redirect('list_of_teachers')


@login_required()
def get_all_students_per_teachers(request, pk):
    all_students_per_teacher = Student.objects.filter(teacher_id=pk)
    return render(request, 'teacher/students_per_teacher.html', {'students_per_teacher': all_students_per_teacher})


class TeacherApi(APIView):

    def get(self, request):
        queryset = Teacher.objects.all()
        serializer = TeacherSerializer(queryset, many=True)
        return Response(serializer.data)
