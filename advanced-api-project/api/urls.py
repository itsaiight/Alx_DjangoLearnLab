from .views import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import path

urlpatterns = [
    path('books/', ListView.as_view(), name='booklist'),
    path('books/<int:pk>/', DetailView.as_view(), name='bookdetail'),
    path('books/create/', CreateView.as_view, name='bookcreate'),
    path('books/update/<int:pk>/', UpdateView.as_view(), name='bookupdate'),
    path('books/delete/<int:pk>/', DeleteView.as_view(), name='bookdelete'),
]