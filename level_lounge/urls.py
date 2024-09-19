from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create_post/', views.create_post, name='create_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('post/<int:id>/edit/', views.edit_post, name='edit_post'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    ]