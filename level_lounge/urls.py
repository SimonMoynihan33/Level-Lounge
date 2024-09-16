from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('update_info/', views.update_info, name='update_info'),
    ]