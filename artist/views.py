# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from artist.models import Artist
from artist.serializers import ArtistSerializer


class ArtistApi(APIView):

    def get(self, request):
        queryset = Artist.objects.all()
        serializer = ArtistSerializer(queryset, many=True)
        return Response(serializer.data)
