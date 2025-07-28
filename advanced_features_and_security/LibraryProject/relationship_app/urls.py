from django.urls import path
from .views import list_books, LibraryDetailView, admin_view, librarian_view, member_view
from django.contrib.auth import views 

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
    path('register/', views.register,template_name='relationship_app/register.html', name='register'),
    path('login/', views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin-dashboard/', admin_view, name='admin_view'),
    path('librarian-dashboard/', librarian_view, name='librarian_view'),
    path('member-dashboard/', member_view, name='member_view'),
    path('books/add_book/', views.add_book, name='add_book'),
    path('books/<int:book_id>/edit_book/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete_book/', views.delete_book, name='delete_book'),


]