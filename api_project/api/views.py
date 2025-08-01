from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]  # Only admin users can perform create, update, delete actions
        
    def get_queryset(self):
        return Book.objects.all()
    def perform_create(self, serializer):
        serializer.save()  # Save the book instance
    def perform_update(self, serializer):
        serializer.save()
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    