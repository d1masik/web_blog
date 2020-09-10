from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('tag/<slug:tag_slug>/', views.post_list, name='posts_with_tag'),
]
