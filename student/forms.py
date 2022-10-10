from django import forms
from django.forms import TextInput, EmailInput, Textarea, DateInput, Select

from student.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'age', 'email', 'is_olympic', 'description', 'start_date', 'end_date',
                  'gender', 'teacher']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'age': TextInput(attrs={'placeholder': 'Please enter your age', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter your description', 'class': 'form-control'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': Select(attrs={'class': 'form-select'}),
            'teacher': Select(attrs={'class': 'form-select'})
        }
    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     get_first_name = cleaned_data.get('first_name')
    #     get_last_name = cleaned_data.get('last_name')
    #     get_email = cleaned_data.get('email')
    #     get_start_date = cleaned_data.get('start_date')
    #     get_end_date = cleaned_data.get('end_date')
    #
    #     if get_start_date > get_end_date:
    #         msg = "Start date can't be bigger than end date."
    #         self._errors['start_date'] = self.error_class([msg])
    #
    #     all_students = Student.objects.all()
    #     for student in all_students:
    #         if get_first_name == student.first_name and get_last_name == student.last_name:
    #             msg = 'Student already exists in the database.'
    #             self._errors['first_name'] = self.error_class([msg])
    #         if get_email == student.email:
    #             msg = 'Email already exists in the database.'
    #             self._errors['email'] = self.error_class([msg])
    #
    #     return cleaned_data

    def clean(self):
        cleaned_data = self.cleaned_data
        get_first_name = cleaned_data.get('first_name')
        get_last_name = cleaned_data.get('last_name')
        get_start_date = cleaned_data.get('start_date')
        get_end_date = cleaned_data.get('end_date')
        get_email = cleaned_data.get('email')
        all_students = Student.objects.all()
        for student in all_students:
            if get_first_name == student.first_name and get_last_name == student.last_name:
                msg = 'There is already a first name and last name in our database'
                self._errors['first_name'] = self.error_class([msg])

            # if get_email == student.email:
            #     msg = 'Email address already used'
            #     self._errors['email'] = self.error_class[msg]

        if get_start_date > get_end_date:
            message = 'The start date is greater than the end date'
            self._errors['start_date'] = self.error_class([message])

        return cleaned_data


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'age', 'email', 'is_olympic', 'description', 'start_date', 'end_date',
                  'gender', 'teacher']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'age': TextInput(attrs={'placeholder': 'Please enter your age', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter your description', 'class': 'form-control'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': Select(attrs={'class': 'form-select'}),
            'teacher': Select(attrs={'class': 'form-select'})
        }
