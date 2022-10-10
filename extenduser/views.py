from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from extenduser.forms import ExtenduserForm
from extenduser.models import ExtendUser


class ExtenduserCreateView(CreateView):
    template_name = 'extenduser/create_user.html'
    model = ExtendUser
    form_class = ExtenduserForm
    success_url = reverse_lazy('login')
