from django.db import models

from teacher.models import Teacher


class Student(models.Model):
    gender_choices = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'))

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=40)
    is_olympic = models.BooleanField(default=False)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    gender = models.CharField(max_length=6, choices=gender_choices)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
