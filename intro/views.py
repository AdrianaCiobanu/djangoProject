from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


@login_required()
def hello(request):
    return HttpResponse('<h1>Hello, Dana!</h1>')


@login_required()
def ciao(request):
    return HttpResponse('<h1>Ciao, Dana!</h1>')


@login_required()
def cars(request):
    context = {
        "all_cars": [
            {
                "name": "Dacia",
                "model": "Logan",
                "color": "White"
            },

            {
                "name": "Tesla",
                "model": "S",
                "color": "Red"
            }

        ]
    }
    return render(request, "intro/cars.html", context)


@login_required()
def movies(request):
    list_movies = {
        "favourite_movies": [
            {
                "name": "Interstellar",
                "director": "Christopher Nolan",
                "year": 2014
            },
            {
                "name": "Inception",
                "director": "Christopher Nolan",
                "year": 2010
            },
            {
                "name": "The Great Dictator",
                "director": "Charles Chaplin",
                "year": 1940
            }
        ]
    }
    return render(request, "intro/movies.html", list_movies)


