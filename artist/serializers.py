from rest_framework import serializers

from artist.models import Artist


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'song', 'album']
