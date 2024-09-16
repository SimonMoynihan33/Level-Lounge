from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create_post/', views.create_post, name='create_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('post/<int:id>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:id>/delete/', views.delete_post, name='delete_post'),
    ]