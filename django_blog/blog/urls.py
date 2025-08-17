from django.urls import path
from django.contrib.auth import views
from .views import SignUpView, ProfileView,PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('register/', SignUpView.as_view(template_name='blog/register.html'), name='register'),
    path('profile/', ProfileView.as_view(template_name='blog/profile.html'), name='profile'),
    path('logout/', views.LogoutView.as_view(next_page='login'), name='logout'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
]