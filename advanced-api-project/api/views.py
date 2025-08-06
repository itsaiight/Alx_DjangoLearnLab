from django.shortcuts import render
from rest_framework import generics, viewsets, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
import django_filters



# Create your views here.
class BookFilter(django_filters.FilterSet):
    publication_year = django_filters.NumberFilter(field_name='published_date', lookup_expr='year')

    class Meta:
        model = Book
        fields = {
            'title': ['exact', 'icontains'],
            'author__name': ['exact', 'icontains'],
            'published_date': ['exact'],
        }
        
# ListView for listing all books
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_class = BookFilter
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'published_date']
    ordering = ['title']
    
# DetailView for retrieving a single book by its primary key
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# CreateView for creating a new book
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    # Override perform_create to handle additional logic if needed
    def perform_create(self, serializer):
        return super().perform_create(serializer)

# UpdateView for updating an existing book
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    # Override perform_update to handle additional logic if needed
    def perform_update(self, serializer):
        return super().perform_update(serializer)

# DeleteView for deleting a book
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]