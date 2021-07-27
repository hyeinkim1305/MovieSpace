from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('<str:username>/', views.profile, name='profile'),
    # path('<int:user_pk>/', views.username, name="username"),
    path('<str:username>/follow/', views.follow, name="follow"),     # 팔로우 기능
    path('<str:username>/follow_info/', views.follow_info, name="follow_info"),      # 팔로워수, 팔로우수
    path('<str:username>/like_genre/', views.like_genre, name="like_genre"),         # 좋아하는 장르 선택해서 DB 저장
    path('<str:username>/recommend/', views.movie_recommend, name="movie_recommend"),
    path('<str:username>/profile/', views.update_user, name="update_user"),
]
