from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from .serializers import UserSerializer, ProfileSerializer, SignUpSerializer, UpdateSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model 
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from movies.models import Genre, Movie
from movies.serializers import GenreSerializer, MovieSerializer
from django.contrib.auth.hashers import check_password


@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 조회시 유저네임, 이메일, 이미지, 인토로덕션 나옴
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    serializer = ProfileSerializer(person)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def follow(request, username):
    you = get_object_or_404(get_user_model(), username=username)
    me = request.user
    # print(me.pk)
    if you != me:
        if you.followers.filter(pk=me.pk).exists():
            you.followers.remove(me)
            # 아래 userfollow는 필요할 것 같아서 넣음
            isFollowed = False
        else:
            you.followers.add(me)
            isFollowed = True
        data = {
            'isFollowed': isFollowed,
            'followers_count' : you.followers.count(),
            'followings_count' : you.followings.count(),
        }
        return Response(data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def follow_info(request, username):
    you = get_object_or_404(get_user_model(), username=username)
    me = request.user
    followers_count = you.followers.count()
    followings_count = you.followings.count()
    if you.followers.filter(pk=me.pk).exists():
        isFollowed = True
    else:
        isFollowed = False
    # 아래 you 정보는 혹시 필요할까봐 넣음
    serializer = UserSerializer(you)
    data = {
        'isFollowed' : isFollowed,
        'followers_count' : followers_count,
        'followings_count' : followings_count,
        'you_info' : serializer.data
    }
    return Response(data)


# 유저가 좋아하는 장르들
@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like_genre(request, username):
    me = get_object_or_404(get_user_model(), username=username)
    if request.method == 'GET':
        serializer = UserSerializer(me)
        return Response(serializer.data)
    elif request.method == 'POST':
        me.like_genres.clear()
        datas = request.data
        for data in datas:
            me.like_genres.add(data)
        return Response({'check':'success'}, status=status.HTTP_201_CREATED)


# 유저가 좋아하는 장르 기반 영화 추천
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_recommend(request, username):
    me = get_object_or_404(get_user_model(), username=username)
    # print(me.like_genres)
    serializer = UserSerializer(me)
    genres = serializer.data.get('like_genres')
    # print(genres)
    movielist = []
    for ge in genres:
        genre = get_object_or_404(Genre, pk=ge)
        movies = genre.movie_set.all()
        movies = MovieSerializer(movies,many=True)
        # return Response(movies.data)
        movielist.append(movies.data)
        # print(genre.title)
    data={
        'data': movielist,
    }
    return Response(data)

@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def update_user(request, username):
    if request.method == 'PUT':
        person = get_object_or_404(get_user_model(), username=username)
        password = request.data.get('password')
        print(request.data)
        if check_password(password, person.password):
            serializer = UpdateSerializer(person, data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                user.set_password(request.data.get('password'))
                user.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        user = request.user
        request.user.delete()
        data ={
            'delete':f'사용자 {user.username} 님이 계정을 삭제하셨습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)