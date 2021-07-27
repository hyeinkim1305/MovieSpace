from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Genre

# 사용자 - 서로 간에 팔로우 가능


class User(AbstractUser):
    followers = models.ManyToManyField(
        'self', symmetrical=False, related_name='followings')
    image = models.CharField(max_length=100, null=True)
    introduction = models.TextField(null=True)
    birth = models.DateField(null=True)
    like_genres = models.ManyToManyField(Genre)
