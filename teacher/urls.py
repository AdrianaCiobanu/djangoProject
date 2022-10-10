from django.urls import path

from teacher import views

urlpatterns = [
    path('create-teacher/', views.TeacherCreateView.as_view(), name='create-teacher'),
    path('list-of-teachers/', views.TeachersListView.as_view(), name='list_of_teachers'),
    path('update-teacher/<int:pk>', views.TeacherUpdateView.as_view(), name='update_teacher'),
    path('details-teacher/<int:pk>', views.TeacherDetailView.as_view(), name='details_teacher'),
    path('delete-teacher/<int:pk>', views.TeacherDeleteView.as_view(), name='delete_teacher'),
    path('delete-modal-teacher/<int:pk>', views.delete_teacher, name='delete_modal_teacher'),
    path('students-per-teacher/<int:pk>', views.get_all_students_per_teachers, name='students_per_teacher'),
    path('teacher-api/', views.TeacherApi.as_view(), name='teacher_api')

]
