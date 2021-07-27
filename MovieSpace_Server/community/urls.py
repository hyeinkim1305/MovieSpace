from django.conf.urls import url
from django.urls import path
from . import views

app_name='community'
urlpatterns = [
    path('', views.article_list_create, name="article_list_create"),
    path('<int:article_pk>/', views.article_detail, name="article_detail"),
    path('<int:article_pk>/comment/', views.comment_list_create, name="comment_list_create"),
    path('<int:article_pk>/comment/<int:comment_pk>/', views.comment_detail, name="comment_detail"),
]
