from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
"""Step 2: Configure User Authentication
User Model and Authentication:
Create a custom user model that extends Django’s AbstractUser, adding fields such as bio, profile_picture, and followers (a ManyToMany field referencing itself, symmetrical=False).
Set up Django REST Framework’s token authentication by adding 'rest_framework.authtoken' to your installed apps and running migrations to create the token model.
Step 3: Define URL Patterns
Routing Configuration:
Configure URL patterns in accounts/urls.py to include routes for registration (/register), login (/login), and user profile management (/profile).
Ensure that registration and login endpoints return a token upon successful operations.
"""
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField("self", symmetrical=False, related_name="following", blank=True)

    def __str__(self):
        return self.username