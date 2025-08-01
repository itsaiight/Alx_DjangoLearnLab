from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()
    def perform_create(self, serializer):
        serializer.save()  # Save the book instance
    def perform_update(self, serializer):
        serializer.save()
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    