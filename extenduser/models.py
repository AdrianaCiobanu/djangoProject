from django.contrib.auth.models import User
from django.db import models


class ExtendUser(User):
    gender_choices = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'))
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=6, choices=gender_choices)
    email_confirm = models.EmailField(max_length=50)
    birthday = models.DateField()

    def __str__(self):
        return self.username


