from django.urls import path
from django.contrib.auth import views
from .views import (
    SignUpView,
    ProfileView, 
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView, 
    CommentCreateView, 
    CommentUpdateView, 
    CommentDeleteView,
    PostSearchView,
    PostsByTagView
)

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('register/', SignUpView.as_view(template_name='blog/register.html'), name='register'),
    path('profile/', ProfileView.as_view(template_name='blog/profile.html'), name='profile'),
    path('logout/', views.LogoutView.as_view(next_page='login'), name='logout'),
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('search/', PostSearchView.as_view(), name='post_search'),
    path('tags/<slug:tag_slug>/', PostsByTagView.as_view(), name='posts_by_tag'),
    
]