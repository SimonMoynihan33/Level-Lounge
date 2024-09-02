from django.contrib import admin
from .models import UserProfile, Post, comment

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(comment)
