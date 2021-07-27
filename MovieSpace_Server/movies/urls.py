from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    # 전체 영화 목록 => 홈화면 carousel
    path('', views.movie_list, name="movie_list"),
    path('genres/', views.genres_list, name="genres_list"),
    path('<int:movie_pk>/', views.movie_detail, name="movie_detail"),
    path('<int:movie_pk>/review/', views.review_list_create, name="review_list_create"),
    path('<int:movie_pk>/review/<int:review_pk>/', views.review_detail, name="review_detail"),
    # 좋아요 추가
    path('<int:movie_pk>/like/', views.like, name="like"),          # like count, likeuser 가져옴
    path('<int:movie_pk>/movie_like/', views.movie_like, name="movie_like"),        # liked 
    path('<str:movie_title>/search/', views.search, name="search"),
    path('best/', views.best_movies, name="best_movies"),
    path('<str:username>/playlist/', views.playlist, name="playlist"),              # 나의 플레이리스트
    path('<str:username>/playlist/<playlist_pk>', views.playlist_detail, name="playlist_detail"),
    path('<str:username>/<int:playlist_pk>/movies/', views.playlist_movies, name="playlist_movies"),        # 나의 플레이리스트에 있는 영화들
    path('<str:username>/<int:playlist_pk>/<int:movie_pk>/', views.playlist_movie, name="playlist_movie"),              # 특정 플레이리스트에 특정 영화 넣기
    path('reviews/', views.reviews, name="reviews"),
]
