from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # get all users the current user follows
        following_users = self.request.user.following.all()
        # filter posts by those authors, ordered by newest first
        return Post.objects.filter(author__in=following_users).order_by("-created_at")