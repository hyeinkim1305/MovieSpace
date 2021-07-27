from rest_framework import serializers
from .models import Article, Comment


# 한번 수정해야할듯 - fields, read_only_fields 등등
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'username')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at','updated_at', 'username')
        # article이랑 user는 빼나??

