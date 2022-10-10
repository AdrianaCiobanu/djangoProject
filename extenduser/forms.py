from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, DateInput

from extenduser.models import ExtendUser


class ExtenduserForm(UserCreationForm):
    class Meta:
        model = ExtendUser
        fields = ['first_name', 'last_name', 'email', 'username', 'email_confirm', 'phone_number', 'gender', 'birthday']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Please enter your username', 'class': 'form-control'}),
            'email_confirm': EmailInput(
                attrs={'placeholder': 'Please enter the email address', 'class': 'form-control'}),
            'phone_number': TextInput(attrs={'placeholder': 'Please enter your phone number', 'class': 'form-control'}),
            'gender': Select(attrs={'class': 'form-control'}),
            'birthday': DateInput(attrs={'class': 'form-control', 'type': 'date'})

        }

    def __init__(self, *args, **kwargs):
        super(ExtenduserForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        self.fields['password1'].widget.attrs['placeholder'] = 'Please enter a password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Please enter a password confirmation'

    def clean(self):
        cleaned_data = self.cleaned_data
        get_email = cleaned_data.get('email')
        all_users = User.objects.all()
        for user in all_users:
            if get_email == user.email:
                message = 'There is already registered a user with this email in our database!'
                self._errors['email'] = self.error_class([message])

        return cleaned_data
