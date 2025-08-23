from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
# Create your views here.
'''implement views and serializers in the accounts app for user registration, login, and token retrieval.'''

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = CustomUser.objects.get(username=response.data["username"])
        token, created = Token.objects.get_or_create(user=user)
        return Response({"user": response.data, "token": token.key})


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({"user": UserSerializer(user).data, "token": token.key})


class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def follow_user(self,  request, user_id):
        target_user = get_object_or_404(User, id=user_id)

        if target_user == request.user:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        request.user.following.add(target_user)
        return Response(
            {"detail": f"You are now following {target_user.username}"},
            status=status.HTTP_200_OK,
        )


class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def unfollow_user(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)

        if target_user == request.user:
            return Response(
                {"detail": "You cannot unfollow yourself."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        request.user.following.remove(target_user)
        return Response(
            {"detail": f"You have unfollowed {target_user.username}"},
            status=status.HTTP_200_OK,
        )