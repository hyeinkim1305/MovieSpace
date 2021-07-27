from django.db import models
from django.conf import settings

# 장르
class Genre(models.Model):
    name = models.CharField(max_length = 50)

# 영화 - popular 기반
class Movie(models.Model):
    # movie_id = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    backdrop_path = models.CharField(max_length=500, null=True)
    video = models.BooleanField()
    vote_average = models.CharField(max_length=5)
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre)
    adult = models.BooleanField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies")

    def __str__(self):
        return self.title

# 나의 영화 리스트
class MyPlayList(models.Model):
    list_name = models.CharField(max_length=100)
    list_description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="lists")
    movies = models.ManyToManyField(Movie)

# 영화에 대한 한줄평
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.IntegerField()
    content = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=200)
