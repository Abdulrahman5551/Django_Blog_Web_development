from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('post/create/', views.createPost, name="post-create"),
    path('post/edit/<int:id>/', views.editPost, name="post-edit"),
    path('post/delete/<int:id>/', views.deletePost, name="post-delete"),
    path('post/about/', views.about, name="about"),
]