from rest_framework import serializers
from .models import Movie, Review, Genre, MyPlayList


# MyMovieList에 대한 serializer 빠짐

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'score', 'content', 'created_at', 'updated_at', 'username')

class MyPlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPlayList
        fields = ('id', 'list_name', 'list_description')