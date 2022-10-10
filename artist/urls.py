from django.urls import path

from artist import views

urlpatterns = [
    path('artist-api/', views.ArtistApi.as_view(), name='artist_api')

]
