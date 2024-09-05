from django.contrib import admin
from .models import UserProfile, Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_at')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_at',)
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Comment)