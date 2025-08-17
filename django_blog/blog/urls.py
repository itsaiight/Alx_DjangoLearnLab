from django.urls import path
from django.contrib.auth import views
from .views import SignUpView, ProfileView

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('register/', SignUpView.as_view(template_name='blog/register.html'), name='register'),
    path('profile/', ProfileView.as_view(template_name='blog/profile.html'), name='profile'),
    path('logout/', views.LogoutView.as_view(next_page='login'), name='logout'),
]