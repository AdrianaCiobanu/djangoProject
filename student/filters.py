import django_filters
from django import forms
from django_filters import DateFilter

from student.models import Student


class StudentFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    start_date__gte = DateFilter(field_name='start_date', lookup_expr='gte',
                                 widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    start_date__lte = DateFilter(field_name='start_date', lookup_expr='lte',
                                 widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    end_date__gte = DateFilter(field_name='end_date', lookup_expr='gte',
                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date__lte = DateFilter(field_name='end_date', lookup_expr='lte',
                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'start_date__gte', 'start_date__lte', 'end_date__gte',
                  'end_date__lte', 'gender']

    def __init__(self, *args, **kwargs):
        super(StudentFilter, self).__init__(*args, **kwargs)

        self.filters['first_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter first name'})
        self.filters['last_name'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter last name'})
        self.filters['age'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter age'})
        self.filters['gender'].field.widget.attrs.update({'class': 'form-control'})
