from django.urls import path
from django.contrib.auth import views
from .views import SignUpView, ProfileView,PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

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
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('comment/<int:pk>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    
]