from itsdangerous import Serializer
from movies.serializers import MovieSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from .models import Movie, Genre, Review, MyPlayList
from .serializers import MovieSerializer, GenreSerializer, ReviewSerializer, MyPlaylistSerializer
from django.contrib.auth import get_user_model 
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from .serializers import UserSerializer,

# 영화 전체 리스트
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])

def genres_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_list_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        reviews = movie.review_set.all().order_by('-pk')
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data) 
    else:
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # print(serializer)
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_detail(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    # if not request.user.review_set.filter(pk=review_pk).exists():
    #     return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # print(request.data)
        serializer = ReviewSerializer(review, data=request.data)
        # print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete': f' 한줄평 {review_pk} 번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    data = {
        'count': movie.like_users.count(),
        'movie': serializer.data,
    }
    return Response(data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    # 유저가 좋아하는 영화
    # user = get_object_or_404(get_user_model(), pk=request.user.pk)
    # print(user.like_movies.all())
    # print(request.user)
    # print(request.user.pk)
    serializer = MovieSerializer(movie)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
        liked=False
    else:
        movie.like_users.add(request.user)
        liked=request.user.pk
    data = {
        'liked': liked,
        'likedcount' : movie.like_users.count()
    }
    return Response(data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def search(request, movie_title):
    movie = get_object_or_404(Movie, title=movie_title)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

# 베스트 영화 추천
@api_view(['GET'])
def best_movies(request):
    movies = Movie.objects.all().order_by('-vote_average')[20:]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def reviews(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)            

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def playlist(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    if request.method == 'GET':
        # 내가 가지고 있는 모든 플레이리스트들
        playlists = MyPlaylistSerializer(user.lists.all(), many=True)
        return Response(playlists.data)
    elif request.method == 'POST':
        # 새로운 플레이리스트 생성 
        serializer = MyPlaylistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def playlist_detail(request, username, playlist_pk):
    user = get_object_or_404(get_user_model(), username=username)
    playlist = get_object_or_404(MyPlayList, pk=playlist_pk)
    if request.method == 'DELETE':
        if playlist.user == user:
            playlist.delete()
            data = {
                'delete': f' 플레이리스트 {playlist.list_name} 이 삭제되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def playlist_movie(request, username, playlist_pk, movie_pk):
    user = get_object_or_404(get_user_model(), username=username)
    # 원래는 user로도 자신의 playlist가 맞는지 한번 걸러줘야 함(시간상 넘어감)
    playlist = get_object_or_404(MyPlayList, pk=playlist_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        if not playlist.movies.filter(pk=movie.pk).exists():
            playlist.movies.add(movie)
            return Response(request.data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def playlist_movies(request, username, playlist_pk):
    user = get_object_or_404(get_user_model(), username=username)
    playlist = get_object_or_404(MyPlayList, pk=playlist_pk)
    print(playlist.movies.all())
    if request.method == 'GET':
        # serializer = MyPlaylistSerializer(playlist.movies.all(), many=True)
        data = {
            'myMovies': playlist.movies.values()
        }
        return Response(data)