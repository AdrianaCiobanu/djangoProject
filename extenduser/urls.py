from django.urls import path

from extenduser import views

urlpatterns = [
    path('create-user/', views.ExtenduserCreateView.as_view(), name='create_user'),

]
