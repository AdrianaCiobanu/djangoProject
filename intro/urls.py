from django.urls import path

from intro import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('ciao/', views.ciao, name='ciao'),
    path('all-cars/', views.cars, name='all_cars'),
    path('favourite-movies/', views.movies, name='favourite_movies'),

]
