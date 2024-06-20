# blog/urls.py
from django.urls import path, include
from . import views, api_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),
    path('search/', views.post_search, name='post_search'),
    path('post/<int:pk>/like/', views.post_like, name='post_like'),
    path('post/<int:pk>/bookmark/', views.post_bookmark, name='post_bookmark'),
    path('api/comments/', api_views.CommentList.as_view(), name='comment_list_api'),
    path('api/comments/<int:pk>/', api_views.CommentDetail.as_view(), name='comment_detail_api'),
    path('api/profiles/<int:pk>/', api_views.ProfileDetail.as_view(), name='profile_detail_api'),
    path('api/posts/', api_views.PostList.as_view(), name='post_list_api'),
    path('api/posts/<int:pk>/', api_views.PostDetail.as_view(), name='post_detail_api'),
    path('accounts/', include('django.contrib.auth.urls')),
]
