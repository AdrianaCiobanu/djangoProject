from django import forms
from django.forms import TextInput, Textarea, TimeInput

from teacher.models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'department', 'course', 'description', 'time']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'department': TextInput(attrs={'placeholder': 'Please enter your department', 'class': 'form-control'}),
            'course': TextInput(attrs={'placeholder': 'Please enter your course', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter course description', 'class': 'form-control'}),
            'time': TimeInput(attrs={'class': 'form-control', 'type': 'time'}),

        }

    def clean(self):
        cleaned_data = self.cleaned_data
        get_first_name = cleaned_data.get('first_name')
        get_last_name = cleaned_data.get('last_name')
        get_course = cleaned_data.get('course')

        all_teachers = Teacher.objects.all()

        for teacher in all_teachers:
            if get_first_name == teacher.first_name and get_last_name == teacher.last_name:
                msg = 'There is already a first name and a last name in our database'
                self._errors['first_name'] = self.error_class([msg])

        return cleaned_data


class TeacherUpdateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'department', 'course', 'description', 'time']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'department': TextInput(attrs={'placeholder': 'Please enter your department', 'class': 'form-control'}),
            'course': TextInput(attrs={'placeholder': 'Please enter your course', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter course description', 'class': 'form-control'}),
            'time': TimeInput(attrs={'class': 'form-control', 'type': 'time'}),

        }
