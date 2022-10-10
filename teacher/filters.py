import django_filters

from teacher.models import Teacher


class TeacherFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'department', 'course']

    def __init__(self, *args, **kwargs):
        super(TeacherFilter, self).__init__(*args, **kwargs)
        self.filters['first_name'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter first name'})
        self.filters['last_name'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter last name'})
        self.filters['department'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter department'})
        self.filters['course'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter course'})

