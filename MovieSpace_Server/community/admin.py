from django.contrib import admin
from .models import Article, Comment
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'content',
        'created_at',
        'updated_at',
        'username',
    ]
    
    def __str__(self):
        return self.title

admin.site.register(Article)
admin.site.register(Comment)
