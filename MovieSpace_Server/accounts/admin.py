from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'username',
        'password',
        'last_name',
        'birth',
        'image',
        'introduction'
    ]

    def __str__(self):
        return self.id

admin.site.register(User)